class Solution {
    public int uniquePaths(int m, int n) {
        Integer [][] dp= new Integer [m][n];
        // Arrays.fill(dp,-1);
        return ways(0,0,m,n,dp);
    }

    // State: at 0,0 Choice :  botton-right i,j+1 i+1,j
    // recurence   i,j+1 i+1,j travese 
    // basecase: 
        // destination : i==m-1 && j=n-1 return 1 ; 
        // crossboundry : i> m-1 || j>n-1 return 0
    // ways(i,j,dp)
    // memeorizayton optimzation :: ways(i+1,j,dp) ,ways(i,j+1,dp)

    int ways(int i, int j, int m,int n ,Integer [][]dp){

        if(i== m-1 && j == n-1) return 1;

        if(i>m-1 || j>n-1) return 0;

        if(dp[i][j] != null )  return dp[i][j];

        dp[i][j]=  ways(i+1,j,m,n,dp)+ways(i,j+1,m,n,dp);
        
        return dp[i][j];
    }


}