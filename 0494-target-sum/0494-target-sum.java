class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        return Solve(0,nums,target);
    }
    // S at i, Choice : take (+) or skip(-)
    // recurrence: Solve(i+1,nums,remaingTarget-nums[i]) Solve(i+1,nums,remaingTarget)
    // BaseCase if(remaingTarget<0 || i==nums.length()) return 0;, if(remaingTarget==0) return 1;
    //


    int Solve(int i,int[] nums,int remaingTarget){

        if(i==nums.length) return remaingTarget == 0 ? 1 : 0;

        int plus= Solve(i+1,nums,remaingTarget+nums[i]);
        int minus= Solve(i+1,nums,remaingTarget-nums[i]);

        return plus+minus;
    }
    
}