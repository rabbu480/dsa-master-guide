class Solution {
    public int[] productExceptSelf(int[] nums) {
      

          int n = nums.length;
        int[] result = new int[n];
        result[0]=1;
        for(int i=1;i<n ; i++ ){
            result[i]=result[i-1]*nums[i-1];
        }
        System.out.println(Arrays.toString(result));
        int[] right = new int[n];
        right[n-1] = 1;
        int j=n-1;
        while(j>0){
            right[j-1]=right[j]*nums[j];
            result[j-1]=right[j-1]*result[j-1];
            j--;
        }
        System.out.println(Arrays.toString(right));
        //agin for loop while :( not neee
        return result;
        
    }
}