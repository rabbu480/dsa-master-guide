class Solution {
    public int maxCoins(int[] nums) {
        int[] arr = new int[nums.length + 2];
        arr[0] = 1;
        arr[arr.length - 1] = 1;

        for (int i = 0; i < nums.length; i++) {
            arr[i + 1] = nums[i];
        }

        int [][] dp = new int [arr.length][arr.length];
        for(int[] col:dp) {
            Arrays.fill(col,-1);
        }
        return Solve(0,arr.length-1,arr,dp);
    }
    // S: i,j
    // choice: k ballon burst
    // recursion : nums[i]*nums[k]*nums[j] +solve(i,k)+solve(k,j)
    // basecase: if i==j return 0;

    int Solve(int i,int j ,int[] nums,int[][] dp) {
        if (i+1==j) return 0 ;
        //  if (i== k || j==k ) return 1 ;
        int maxCoins=0;
        if(dp[i][j] !=-1) return dp[i][j];
        for(int k=i+1 ; k< j ; k++) {
           int cost=nums[i]*nums[k]*nums[j] +Solve(i,k,nums,dp)+Solve(k,j,nums,dp);
           dp[i][j]=maxCoins=Math.max(maxCoins,cost);
        }
        return dp[i][j];
    }
}