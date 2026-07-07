class Solution {
    public int[] twoSum(int[] numbers, int target) {

        // O(n),O(n)
        // Map<Integer,Integer> numMap= new HashMap<>();
        // for(int i =0 ; i< numbers.length ; i++){
        //     if(numMap.containsKey(target-numbers[i])){
        //         int[] result= new int[2];
        //         result[0]=numMap.get(target-numbers[i])+1;
        //         result[1]=i+1;
        //         return result; 
        //         // retun new Integer { numMap.containsKey(target-numbers[i]) ,i  } ;
        //     }
        //     numMap.put(numbers[i],i);
        // }
        // return null;
        
        // Via two pointer: O(n2)
        // for(int i = 0; i < numbers.length ; i++){
        //     int j = i+1;
        //     while(j < numbers.length){
        //         if(numbers[i] + numbers[j]==target){
        //             int[] result= new int[2];
        //             result[0]= i+1;
        //             result[1]=j+1;
        //             return result;
        //         }
        //         j++;
        //     }
        // }
        // return null;

        // O(n) O(1)
        int right = numbers.length-1;
        int left = 0; 
        while(left < right){
            int sum =numbers[left]+numbers[right];
            if(sum == target){
                return new int[]{left+1,right+1};
            }
            if(sum < target){
                left++;
            } else if(sum > target ){
                right --;
            }
        }

        return null;

    }
}