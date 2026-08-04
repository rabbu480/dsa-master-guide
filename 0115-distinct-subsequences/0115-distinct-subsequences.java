class Solution {
    public int numDistinct(String s, String t) {
        int[][] dp= new int[s.length()][t.length()];
        for(int[] col: dp){ Arrays.fill(col,-1);}

        return Solve(0,0,s,t,dp);
    }
    // convert Source to Target
    // S : i,j  Chocice take ,skip  
    // R : if (source.charAt(i)==target.charAt(j)) Solve(i+1,j+1,source,target)  Match again then skip Solve(i+1,j,source,target), NO match then Solve(i+1,j,source,target)
    // Basecase if(i == source.length()) return 0 if(j == target.length()) return 1;

    int Solve(int i, int j , String source,String target,int[][] dp){

        if(j == target.length()) return 1;
        if(i == source.length()) return 0;

        if(dp[i][j] != -1) return dp[i][j];

        if (source.charAt(i)==target.charAt(j)) {
            dp[i][j]= Solve(i+1,j+1,source,target,dp)+Solve(i+1,j,source,target,dp);
            return dp[i][j];
        }
        
        dp[i][j]=Solve(i+1,j,source,target,dp);
        
        return dp[i][j];
    }
}