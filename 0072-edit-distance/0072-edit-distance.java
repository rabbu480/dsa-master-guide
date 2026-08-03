class Solution {
    public int minDistance(String word1, String word2) {
        int[][] dp=new int[word1.length()][word2.length()];
        for(int[] col:dp){
            Arrays.fill(col,-1);
        }
        return Solve(0,0,word1,word2,dp);
    }
    // State i, j in word1 & word2 
    // Choice : insert: Solve(i+1,j+1,word1,word2) Delete : Solve(i+1,j,word1,word2)  Replace:Solve(i,j+1,word1,word2)
    // recursion : Solve(i+1,j+1,word1,word2) Delete : Solve(i+1,j,word1,word2)  Replace:Solve(i,j+1,word1,word2)
    // basecase : if(i==word1.length() || j==word2.length()  ) return 0;


    int Solve(int i, int j , String word1, String word2,int[][] dp ){
        // word1 = "" word2 = "abc" to convert insert a then b then c
        if(i == word1.length())
            return word2.length() - j;

        if(j == word2.length())
            return word1.length() - i;

        if(dp[i][j]!=-1) return dp[i][j];

        if(word1.charAt(i) == word2.charAt(j)){
            dp[i][j]= Solve(i+1, j+1, word1, word2,dp);
            return dp[i][j];
        }

        int insert = Solve(i, j+1, word1, word2,dp);

        int delete = Solve(i+1, j, word1, word2,dp);

        int replace = Solve(i+1, j+1, word1, word2,dp);

        dp[i][j]=1+Math.min(insert,Math.min(delete,replace));

        return dp[i][j];
    }
}