class Solution {
    public int longestConsecutive(int[] nums) {
        // dont use arrays.sort o(n logn ) use hashset the o(n)
        Set<Integer> sortedNums= new HashSet<>();
        for(int num:nums){
            sortedNums.add(num);
        }
        int longestConsecutive=0;
        for(int num:sortedNums ){
            int count=1;
            // required to avoid multiple iteration to get start of sequence.
            if(!sortedNums.contains(num-1)){
                while(sortedNums.contains(num+1)){
                    count++;
                    num = num+1;
                }
            }
            longestConsecutive=Math.max(longestConsecutive,count);
        }
        return longestConsecutive;
        
    }
}