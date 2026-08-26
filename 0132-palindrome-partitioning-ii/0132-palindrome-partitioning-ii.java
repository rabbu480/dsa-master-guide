class Solution {
    public int minCut(String s) {
        int n= s.length();
        
        // if this palindom i=0 n j =i+1;
        // if palindrome get the next cut 
        // int count=0;
        // for(int i=0;i<n ; i++){
        //     for(int j=i+1;j<n ; j++){
        //         if(isPlaindrom(i,j,s,dp)){
        //             count=1 + SolveCut(j+1,n);
        //         }
        //     }
        // }
        
        int[] dp1= new int[n];
            Arrays.fill(dp1,-1);
            Boolean[][] dp= new Boolean[n][n];
        return SolveCut(0,s,dp1,dp);
    }

    //returns j 
    // S: i , choice j 
    // R if(isPlaindrom) then choose candidate (nextj) and j j reached last before the dont choose 
    // B  if(i==s.lenth()) return 0
    // R


    int SolveCut(int i,String s,int[] dp1, Boolean[][] dp){
        int n=s.length();
        
        if(dp1[i] != -1) return dp1[i];

        int min = Integer.MAX_VALUE;
        for(int j=i; j<n ; j++){
            if(isPlaindrom(i,j,s,dp)){
                // return 1+SolveCut(j,s);

                int candidate=0;
                if(j != n-1){
                  candidate = 1+ SolveCut(j+1,s,dp1,dp);
                }
                dp1[i]=Math.min(min,candidate );
                min=dp1[i];
            }
        }
        return min;
    }



    boolean isPlaindrom(int i,int j,String s,Boolean[][] dp){
        if(i>= j ) return true;
        if(dp[i][j] != null ) return dp[i][j];
        if(s.charAt(i) != s.charAt(j)) return false;
        dp[i][j]=isPlaindrom(i+1,j-1,s,dp);
        return dp[i][j];
    }

}