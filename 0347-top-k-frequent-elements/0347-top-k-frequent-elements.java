class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        Map<Integer, Integer> freqMap = new HashMap<>();
        // Get Map with freqcies. every insertion O(1) total o(n)
        for(int num : nums){
            freqMap.put(num,freqMap.getOrDefault(num,0)+1);
        }
        //  (a, b) -> Integer.compare(freqMap.get(a), freqMap.get(b))
        PriorityQueue<Integer> pq=new PriorityQueue((a,b) ->  freqMap.get(a) - freqMap.get(b));
        // for (Map.Entry<Integer, Integer> entry : freqMap.entrySet()) {
        //     int key = entry.getKey();
        //     int value = entry.getValue();
        // }
        for(int key: freqMap.keySet()){
            pq.offer(key);
            if(pq.size() > k){
                pq.poll();
            }
        }
        int[] result= new int[pq.size()];
        int i=0;
        while(!pq.isEmpty()){
            result[i]=pq.poll();
            i++;
        }
    return result;

        
    }
}