class Solution {
    // bruite for o(n3) for(i=0)for(j==i) if(isPalindron(i,j,s)) return true;
    // isPalindron(i,j,s) while (i<j) if s.charAt(i) != s.charAt(j) return false; return true; 
   
    public String longestPalindrome(String s) {
        int n=s.length();
        int maxLength=0;
        String str="";
        Boolean[][] dp= new Boolean[n][n];

        for(int i=0; i< n; i++ ){
            for(int j=i; j< n; j++ ){
                if(Solve(i,j,s,dp)) {
                    if(maxLength<j-i+1){
                        maxLength=j-i+1;
                        //Java's substring(start, end) uses an exclusive end index.
                        str=s.substring(i,j+1);
                    }
                }
            }
        }
        return str;
    }

    // State i=0,j=n-1  Choice (Boolean) isPalindrom & nonPalindrom 
    // Recurrence Solve(i+1,j-1) Solve(i,j-1) SOlve(i+1,j)
    // BaseCase : if(i > j ) return true
    // recuursion  if(s.charAt(i) == s.charAt(j))  Solve(i+1,j-1);
    //              return Solve(i,j-1) || Solve(i+1,j)
    //

    boolean Solve(int i,int j,String s,Boolean[][] dp){
        if(i >= j ) return true;
        if(s.charAt(i) != s.charAt(j)) {
            return false;
        }
        if(dp[i][j] != null){
            return dp[i][j];
        }
        dp[i][j]=Solve(i+1,j-1,s,dp);
        return  dp[i][j];
    }


}