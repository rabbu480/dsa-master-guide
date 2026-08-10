class Solution {
    public int findKthLargest(int[] nums, int k) {
        
        // define minHeap PrioityQueue 
         PriorityQueue<Integer> minHeap=new PriorityQueue<>();
        // Maintain a min heap of size k.
        // If the heap grows beyond k,
        // remove the smallest element.
        // The heap always contains the k largest elements.
         // time: O(nlogn) Space: O(k)
        for(int num: nums){
            // O(logk)
            minHeap.offer(num); 
            if(minHeap.size() > k ){
                // O(logk)
                minHeap.poll();
            }
        }

        return minHeap.peek();
    }
}
