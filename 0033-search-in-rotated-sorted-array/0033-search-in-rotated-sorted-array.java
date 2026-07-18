class Solution {
    public int search(int[] nums, int target) {
        int left=0;
        int right= nums.length-1;
        int tergetIndex=-1;
        while(left<=right){
            int mid=left+(right-left)/2;
            if(nums[mid] == target ){
                tergetIndex= mid;
                return mid;
            }
            
            if( nums[left] <= nums[mid]  ){
                // sorted 
                // 4,5,6,7,0,1,2 target=5
                // 
                if( nums[left] <= target && target <= nums[mid]  ){
                    right=mid-1;
                } else {
                    left= mid+1;
                }
            } 

            if( nums[right] >= nums[mid]){
                // sorted 
                // 6,7,0,1,2,3,4 target 3
                // 6,7,8,9,0,1
                if(  nums[mid] <= target  && target <= nums[right] ){
                    left=mid+1;
                } else {
                    right= mid-1;
                }

            }

        }
        return tergetIndex;
    }
}