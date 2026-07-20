class Solution {
    public int rob(int[] nums) {
        int length=nums.length;
        int[] dp= new int[nums.length];
        if (nums.length == 1) return nums[0];
        // 0,1,2 => 6 0,2  1,
        Arrays.fill(dp,-1);
        int robStartAt0=robMaxAmnt(0,length-2,nums,dp);
        System.out.println("dp::>>" +Arrays.toString(dp));
        Arrays.fill(dp,-1);
        int robStartAt1=robMaxAmnt(1,length-1,nums,dp);
        System.out.println("dp::<<" +Arrays.toString(dp));
        return Math.max(robStartAt0,robStartAt1);

    }

    // State 0 i, choice rob or skip  
    // recurrence,basecase, recurssion 
    // memorization 
    int robMaxAmnt(int i,int robTill,int[] nums, int[] dp ){

        if(i > robTill) return 0;

        if(dp[i] != -1){
            return dp[i];
        }

        int skip=robMaxAmnt(i+1,robTill,nums,dp);
        int rob= nums[i]+robMaxAmnt(i+2,robTill,nums,dp);
        dp[i]= Math.max(rob,skip);

        return dp[i];

    }
}