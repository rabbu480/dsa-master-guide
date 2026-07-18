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
            // [4,5,6,7,8,9,0,1,2]
            // check if Left is sorted
            if( nums[left] <= nums[mid]  ){
                // sorted mid is 8 taget 9
                // Left is not sorted i.e right is sorted
                // check if the target in the range then use the half else discard & check next half.
                if( nums[left] <= target && target < nums[mid]  ){
                    right=mid-1;
                } else {
                    left= mid+1;
                }
            } else {
                // Left is not sorted i.e irght is sorted
                // check if the target in the range then use the half else discard go right.
                if(  nums[mid] < target  && target <= nums[right] ){
                    left=mid+1;
                } else {
                    right= mid-1;
                }

            }

        }
        return tergetIndex;
    }
}