class Solution {
    public int numDecodings(String s) {

        int[] dp = new int[s.length()];
        Arrays.fill(dp,-1);

        return decode(0,s,dp);   
    }
    // State , choice :: index i , i+1 or i+2 if valid
    // recurence :: decode i+1 or i+2 
    // Basecase : charAt(i) = 0 then return 0; charAt i > string length return 1 
    // recursion 
    // memorization 
    int decode(int i,String s, int[] dp){

        //Base Condition1
        if(i == s.length() ) return 1;

        //Base Condition2
        if(s.charAt(i) == '0' ) return 0; 

        if(dp[i]!=-1) return dp[i];

        int ways=decode(i+1,s,dp);

        // shoul contain 2 disgits and shoul lessatahn length
        if (i + 1 < s.length()) {
            int val = Integer.parseInt(s.substring(i, i + 2));

            if (val <= 26) {
                ways += decode(i + 2, s, dp);
            }
            System.out.println(" i >> "+i +"val >>"+ val + " dp >> "+Arrays.toString(dp));
        }

        dp[i]=ways;
        return ways;
    }

}