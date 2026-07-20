class Solution {
    public int minCostClimbingStairs(int[] cost) {

        // state 0, 1 this i.e 
        // min(way(0), way(1))
        int[] dp= new int[cost.length];
        Arrays.fill(dp,-1);

        return Math.min(cost(0,cost,dp),cost(1,cost,dp));

        
    }

    // State,Choices: i i.e 0 or 1, one or two steps
    // recurence  
    int cost(int i ,int [] cost,int[] dp){
        if(i>= cost.length) return 0;
        if(dp[i] != -1){
            return dp[i];
        }
        // should save 
        dp[i]=cost[i]+Math.min(cost(i+1,cost,dp),cost(i+2,cost,dp));
        return dp[i];
    }
}