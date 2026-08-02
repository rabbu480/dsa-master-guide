class Solution {
    public int rob(int[] nums) {
        
        int n= nums.length-1;
        if(n==0) return nums[n];
        int[] dp =new int[nums.length];
        Arrays.fill(dp,-1);
        int startAt0= solve(0,n-1,nums,dp);
        Arrays.fill(dp,-1);
        int startAtENd= solve(1,n,nums,dp);
        return Math.max(startAt0,startAtENd);
    }
    // state : ith,,, house choice : rob or skip 
    // recurrence 

    int solve(int i,int robTill, int[] nums,int[] dp){

        if(i > robTill) return 0;
        if(dp[i] != -1) return dp[i];

        int rob=nums[i]+solve(i+2,robTill,nums,dp);
        int skip=solve(i+1,robTill,nums,dp);
        dp[i]=  Math.max(rob,skip);

        return dp[i];
    }
}

