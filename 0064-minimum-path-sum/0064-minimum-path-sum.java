class Solution {
    public int minPathSum(int[][] grid) {
      int[][] dp = new int[grid.length][grid[0].length];
      for(int[] col:dp) { Arrays.fill(col,-1); }
      return pathSum(0,0,grid,dp);
    }

    // s 0,0 c: top left to bottonright 0,j+1 i+1,2
    // 
 
    int pathSum(int i ,int j ,int[][] grid,int[][] dp ){
        int m = grid.length-1;
        int n = grid[0].length-1;
        if(i == m && j  == n) return grid[i][j];
        if(i > m || j > n) return Integer.MAX_VALUE;
        if(dp[i][j] != -1){
            return dp[i][j];
        }
        dp[i][j] = grid[i][j] + Math.min(pathSum(i,j+1,grid,dp), pathSum(i+1,j,grid,dp));
        return dp[i][j]; 
    }
}