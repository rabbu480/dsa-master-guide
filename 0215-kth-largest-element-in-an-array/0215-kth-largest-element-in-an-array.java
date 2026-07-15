class Solution {
    public int findKthLargest(int[] nums, int k) {
        
        // define minHeap PrioityQueue 
         PriorityQueue<Integer> pq=new PriorityQueue<>();
         // maintain minHeap size k 
         // while all elemnts < k remove from queue 
         // so that the the minHeap contain the kth largest at top
         //  elemnt and larget than k
         // time: O(nlogn) Space: O(k)
        for(int num: nums){
            // O(logk)
            pq.offer(num); 
            if(pq.size() > k ){
                // O(logk)
                pq.poll();
            }
        }

        return pq.peek();
    }
}
