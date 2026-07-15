class Solution {
    public int findKthLargest(int[] nums, int k) {
        
        // define minHeap PrioityQueue 
         PriorityQueue<Integer> pq=new PriorityQueue<>();
        // Maintain a min heap of size k.
        // If the heap grows beyond k,
        // remove the smallest element.
        // The heap always contains the k largest elements.
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
