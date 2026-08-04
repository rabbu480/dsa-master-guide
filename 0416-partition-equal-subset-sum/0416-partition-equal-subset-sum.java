class Solution {

    public boolean canPartition(int[] nums) {
        int sum=0;
        for(int num:nums){
            sum+= num;
        }
        if(sum % 2 != 0) return false;
        int target=sum/2;
        Boolean[][] dp= new Boolean[nums.length][target+1];
        return Solve(0,target,nums,dp);
    }
    // State: i , Choice: take , skip 
    // R take : i+1, remaing-nums[i] ,,, skip i+1, remaing.
    // B : BaseCase: if(remain==0) return true ;; if(i==nums.length) return false;
    // Recursion: Solve(i+1,remain-nums[i])  Solve(i+1,remain)

    Boolean Solve(int i,int remainTotal, int[] nums,Boolean[][] dp){

        if(remainTotal == 0) return true ;
        if(remainTotal < 0 || i == nums.length) return false;
        
        if(dp[i][remainTotal] != null){ return dp[i][remainTotal] ; }

        boolean take = Solve(i+1,remainTotal-nums[i],nums,dp);
        boolean skip = Solve(i+1,remainTotal,nums,dp);
        
        dp[i][remainTotal]=take||skip;
        
        return dp [i][remainTotal] ;
    }
}