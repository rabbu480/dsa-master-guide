class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int[][] dp = new int[obstacleGrid.length][obstacleGrid[0].length];
        for(int[] col: dp){
            Arrays.fill(col,-1);
        }
        return ways(0,0,obstacleGrid,dp);
        
    }
    // State 0,0, Choice i+1,j i,j+1
    // Recurrence ways(i+1,j),ways(i,j+1) 
    // BaseCase:    i==m && j==n  rertun 1, i>m || j<n return 0  grid[i][j] ==1 return 0
    // Recurrsion  ways(i+1,j),ways(i,j+1) 
    // abstacle=1 then skip do go

    int ways(int i, int j,int[][] grid,int[][]dp ){
        int m= grid.length-1;
        int n= grid[0].length-1;
        if( i==m && j==n && grid[i][j] != 1)  return 1 ;
        if( i>m || j>n || grid[i][j] == 1)  return 0 ;
        if(dp[i][j] != -1) return dp[i][j];
        dp[i][j]=ways(i+1,j,grid,dp)+ways(i,j+1,grid,dp);
        return dp[i][j];
    }


}