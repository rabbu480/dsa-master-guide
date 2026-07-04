class Solution {
    public int[] twoSum(int[] nums, int target) {

        HashMap<Integer,Integer> hm= new HashMap<>();
        for(int i=0; i<nums.length ; i++ ){
            if(hm.containsKey(nums[i])){
                return new int[] { i , hm.get(nums[i])};
            }
            hm.put(target-nums[i],i);
        }
        return null;
    }

    //         HashMap<Integer,Integer> elementMap= new HashMap<>();

//         for(int i=0; i<nums.length;i++){
//             int secondNum=target-nums[i];
//             if(elementMap.containsKey(secondNum)){
//                 return new int[]{i, elementMap.get(secondNum) };
//             }
//             elementMap.put(nums[i],i);
//         }
//         return null;
}

