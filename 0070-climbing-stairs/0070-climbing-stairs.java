class Solution {
    public int climbStairs(int n) {
        // 4: memorization 
        int[] dp= new int[n+1];
        Arrays.fill(dp, -1);
        // System.out.println(" dp[i]::::"+ Arrays.toString(dp));
        return ways(0,n,dp);
    }

    // state & choice ::  i th position , +1 & +2 
    // Recurrence & Basecase & recursion:: 
    int ways(int i,int n,int[] dp){
        if(i == n) return 1;
        if(i > n ) return 0;
        if(dp[i] != -1 ){
            return dp[i];
        }
        // System.out.println(" dp[i]>>>::::"+i+"---"+ Arrays.toString( dp));
        // complete path after ith step  can tak 1 or 2 like wise each time we checking 
        dp[i]=ways(i+1,n,dp)+ways(i+2,n,dp);
        // System.out.println(" dp[i]>>>::::"+i+"---"+ Arrays.toString( dp));
        // System.out.println(" dp[i]>>>::::"+i+"---"+ dp[i]);
        return dp[i];
    }
}