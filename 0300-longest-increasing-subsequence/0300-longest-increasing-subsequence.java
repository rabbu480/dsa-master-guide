class Solution {
    public int lengthOfLIS(int[] nums) {
        //starts from -1 so 
        int[][] dp= new int[nums.length][nums.length+1];
        for(int[] row : dp){
            Arrays.fill(row,-1);
        }
        // return Solve(0,-1,nums);
        return Solve(0,-1,dp,nums);
    }
    // State i,prev chocie: take the current skip the current   
    // R take Solve(i+1,i)  skip : Solve(i+1,prev) 
    // B : i=nums.length() return =0;
    //2^n && O(n)
    // int Solve(int i,int prev ,int[] nums){

    //     if(i==nums.length){
    //         return 0;
    //     }

    //     int take=0;
    //     if( prev== -1 || nums[i] > nums[prev]){
    //         take = 1+Solve(i+1,i,nums);
    //     }
    //     int skip=Solve(i+1,prev,nums);

    //     return Math.max(take,skip);
    // }

    int Solve(int i,int prev,int[][] dp ,int[] nums){

        if(i==nums.length){
            return 0;
        }

        if(dp[i][prev+1] != -1) return dp[i][prev+1];


        int take=0;
        if( prev == -1 || nums[i] > nums[prev]){
            take = 1+Solve(i+1,i,dp,nums);
        }
        int skip=Solve(i+1,prev,dp,nums);
        dp[i][prev+1] =Math.max(take,skip);

        return dp[i][prev+1];
    }


}