class Solution {
    public boolean containsDuplicate(int[] nums) {

        // for(int i=0; i< nums.length ; i++){
        //     int j=i+1;
        //     while(j <  nums.length){
        //         if(nums[i] == nums[j]){
        //             return true;
        //         }
        //         j++;
        //     }
        // }
        // return false;


        Set<Integer> h= new HashSet();
        for(int i=0; i< nums.length ; i++){
            if(h.contains(nums[i])){
                return true;
            }
            h.add(nums[i]);
        }
        return false;
        
    }
}