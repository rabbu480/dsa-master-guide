class Solution {
    public int findMin(int[] nums) {

        // Find Minimum in Rotated Sorted Array 

// this also while loop 
// same as LC33 get condition where nums[mid] < 
// below are tree possibilities 
// minNumber
// [4,5,6,7,0,1,2]    ==> 
    // nums[left] >= nums[mid]  
    // else here 

        int left=0;
        int right= nums.length-1;
        int mid=0;
        // 0, 6,3   4,7,2
        // 4, 6   if ()
        while(left < right){
            mid=left+(right-left)/2;
            if(nums[left] <= nums[right]){
                return nums[left];
            }
            if(nums[left] <= nums[mid] ){
                left=mid+1;
            } else {
                right=mid;
            } 
        }
        return nums[left];


    }
}