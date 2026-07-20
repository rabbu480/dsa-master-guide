class Solution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp,-1);
        int minCoins=minCoins(coins,amount,dp) ;
        if(minCoins == Integer.MAX_VALUE){
            return -1;
        } 
        return minCoins;
    }

    // state :remainingAmount choices: coins 
    // recurence check fro all teh coins 
    // BaseCase:
    //      if remaing=0 then  return 0 as we dont need coin anymore.
    //      if remaing<0 then  return Math.infinate as thsi impossible to get the exacr change coin anymore.
    // recursion : for each coin check (1+Math.min(coins(remaingAmount));

    int minCoins(int[] coins, int remainingAmount,int[] dp){

        if(remainingAmount==0) return 0;
        if(remainingAmount<0) return Integer.MAX_VALUE;

        

        
        if(dp[remainingAmount] != -1)  return dp[remainingAmount];
        int minCoins=Integer.MAX_VALUE;
        
        // what if pick 1,2,5
        //Because recursion goes all the way down before coming back up.Think about DFS in trees.
        for(int coin: coins) {
            // min coin can get by the amount wh
            int temp= minCoins(coins,remainingAmount-coin,dp);

            if(temp != Integer.MAX_VALUE){    
                minCoins= Math.min(minCoins,1+temp);
                
                // System.out.println("temp >> "+temp +"-> coin " +coin +"-> remainingAmount " + remainingAmount +"-> minCoins :: " +minCoins);

                // minCoins= minCoins == Integer.MAX_VALUE ? -1 : minCoins;
            }
        }
        dp[remainingAmount]=minCoins;

        return dp[remainingAmount];

    }


}