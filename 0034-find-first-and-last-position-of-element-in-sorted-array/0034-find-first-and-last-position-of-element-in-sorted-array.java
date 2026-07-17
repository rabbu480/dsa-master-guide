class Solution {
    public int[] searchRange(int[] nums, int target) {

        int firstOccurence= firstOccurence(nums,target);
        int lastOccurentce = lastOccurence(nums,target);
        

        return new int[]{firstOccurence,lastOccurentce};
    }

    int firstOccurence(int[] nums, int target){
        int left=0;
        int right=nums.length-1;
        int firstOccurence=-1;
        while(left<= right){
            int mid= left+ (right-left)/2;
            if(nums[mid]<target){
                left=mid+1;
            } else if(nums[mid] > target){
                right = mid - 1;
            } else {
                // check is there any element ealier than this 
                firstOccurence=mid;
                right=mid-1;
            }

        }
        return firstOccurence;
    }
    int lastOccurence(int[] nums, int target){
        int left=0;
        int right=nums.length-1;
        int lastOccurence=-1;
        while(left<= right){
            int mid= left+ (right-left)/2;
            if(nums[mid]<target){
                left=mid+1;
            } else if(nums[mid] > target){
                right = mid - 1;
            } else {
                // check is there any element ealier than this 
                lastOccurence=mid;
                left=mid+1;
            }
        }
        return lastOccurence;
    }
}