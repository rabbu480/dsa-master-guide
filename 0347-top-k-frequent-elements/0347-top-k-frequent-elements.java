class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        // as per constraints o(n) we need aim for 
        // so as far as i know get map of frequency conts
        // use heaps for min heap to get only topelevel element i mean top k frequenct
        HashMap<Integer,Integer> freqMap= new HashMap<>();
        for(int num: nums){
            // freqMap.computeIfAbasent(num,1).add(freqMap.get(num)+1);
            freqMap.put(num,freqMap.getOrDefault(num,0)+1);
        }
        // now map has all the values 
        Queue<Integer> freqElements = new PriorityQueue((a,b) ->freqMap.get(a) - freqMap.get(b) );
        //
        // ArrayList<Integer> freqElements = new ArrayList();
        for(int freqKey: freqMap.keySet() ){
            // if(freqMap.get(freqKey) >= k){
                freqElements.offer(freqKey);
                if(freqElements.size() > k ){
                    freqElements.poll();
                }
            // }
        }
        int[] freqElementResult= new int[freqElements.size()];
        int freqElementIndex =0;
        // for(int freqElement:freqElements){
        //     freqElementResult[freqElementIndex]=freqElement;
        //     freqElementIndex++;
        // }
        while(!freqElements.isEmpty()){
            freqElementResult[freqElementIndex]=freqElements.poll();
            freqElementIndex++;
        }
        return freqElementResult;
        
    }
}