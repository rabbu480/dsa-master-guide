class Solution {
    public int[] twoSum(int[] numbers, int target) {

        Map<Integer,Integer> numMap= new HashMap<>();
        for(int i =0 ; i< numbers.length ; i++){
            if(numMap.containsKey(target-numbers[i])){
                int[] result= new int[2];
                result[0]=numMap.get(target-numbers[i])+1;
                result[1]=i+1;
                return result; 
                // retun new Integer { numMap.containsKey(target-numbers[i]) ,i  } ;
            }
            numMap.put(numbers[i],i);
        }
        return null;
        
    }
}