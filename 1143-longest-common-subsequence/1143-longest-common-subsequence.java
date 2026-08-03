class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int[][] dp=new int[text1.length()][text2.length()];
        for(int[] col : dp){
            Arrays.fill(col,-1);
        }

     return Solve(0,0,text1,text2,dp);   
    }

    // State :: i , j from text1,text2 
    // Choice -> if char At i==j 1+solve(i+1,i+j)  take both move next 
    //      char At i!=j check which cuase the sequence break Skip solve(i,1+j), solve(i+1,j)
    // BaseCase i==text1.length() && j== text2.length()  return 0;
    // recursion :  1+solve(i+1,j+1)  Math.max(solve(i,j+1), solve(i+1,j))

    int Solve(int i, int j,String text1, String text2,int[][] dp){

        if(i==text1.length() || j== text2.length())  return 0;
        if(dp[i][j] != -1){
            return dp[i][j] ;
        }
        
        if(text1.charAt(i) == text2.charAt(j) ){
            dp[i][j]= 1+Solve(i+1,j+1,text1,text2,dp);
           return dp[i][j];
        }

        dp[i][j]=Math.max(Solve(i+1,j,text1,text2,dp), Solve(i,j+1,text1,text2,dp));

        return dp[i][j];
    }

}