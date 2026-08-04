class Solution {

    public int findTargetSumWays(int[] nums, int target) {
        // int sum=0;
        // for(int num:nums){
        //     sum+=num;
        // }
        // offset - to + is index so  
        // int[][] dp=new int[nums.length][target+sum];
        Map<String,Integer> dp= new HashMap<>();    
        return Solve(0,nums,target,dp);
    }
    // S at i, Choice : take (+) or skip(-)
    // recurrence: Solve(i+1,nums,remaingTarget-nums[i]) Solve(i+1,nums,remaingTarget)
    // BaseCase if(remaingTarget<0 || i==nums.length()) return 0;, if(remaingTarget==0) return 1;
    //


    int Solve(int i,int[] nums,int remaingTarget,Map<String,Integer> dp){

        if(i==nums.length) {
            if(remaingTarget == 0) return 1;
            return 0;
        } 

        String key= "#"+i+"-"+remaingTarget+"#";

        if(dp.containsKey(key)){
          return  dp.get(key);
        }

        int plus= Solve(i+1,nums,remaingTarget+nums[i],dp);
        int minus= Solve(i+1,nums,remaingTarget-nums[i],dp);
        int result=plus+minus;
        dp.put(key, result);

        return dp.get(key) ;
    }
    
}