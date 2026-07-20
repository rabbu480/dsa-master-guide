class Solution {
    public int rob(int[] nums) {
        int[] dp= new int[nums.length];
        Arrays.fill(dp,-1); 

        return maxAmount(0,nums , dp);
    }
    // State (start from house 0) , Choice (1 skip 2 )  ==> Rob this house OR Skip this house .
    // recurrence, Base codition, recusion 
    // Memorization dp[]  fill -1

    int maxAmount(int i, int[] nums , int[] dp){ 
        if(i>= nums.length) return 0;
        if(dp[i]!=-1){
            return dp[i];
        }
        // either start 1 ,start 2
        // Take nums[i] -> Go to i+2
        // Take Nothing -> Go to i+1
        dp[i]= Math.max(maxAmount(i+1,nums,dp),nums[i]+maxAmount(i+2,nums,dp));
        return dp[i];
    }




}