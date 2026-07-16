class MedianFinder {


    PriorityQueue<Integer> minHeap;
    PriorityQueue<Integer> maxHeap;
    
    public MedianFinder() {
        // store Max elements so : heap contains second half of max numbers
        // maxofSecondHalf= peek
        minHeap= new PriorityQueue<>();
        // store min elements so : heap contains first half of min numbers
        // minofSecondHalf= peek
        maxHeap = new PriorityQueue<>( Collections.reverseOrder() );

        // ==>  // 1,3,5,7,9,10
        // minHeap: 7,9,10  ==> peek ==7
        // maxHeap: 1,3,5   ==> peek ==5
        // initally insert to maxHeap
        // if the number > minheap  remove from minHeap add to maxheap 
        // if the number < maxheap  remove from maxHeap add to minheap 


    }
    
    public void addNum(int num) {
        //1,2,3
        // maxHeap 1,3
        // minHeap 2
        if(maxHeap.isEmpty() || num <= maxHeap.peek()){
            maxHeap.offer(num);
        } else{
            minHeap.offer(num);
        }

        if(maxHeap.size()- minHeap.size()>1){
           minHeap.offer(maxHeap.poll());
        }
        if( minHeap.size()-maxHeap.size()>1){
           maxHeap.offer( minHeap.poll());
        }
    }
    
    public double findMedian() {
        // even: median ==> middle number 
        // odd : median ==> avg of middle numbers
        int minSize=minHeap.size();
        int maxSize=maxHeap.size();
        double median=0;
        if(minSize==maxSize){
           median= (double) (minHeap.peek()+maxHeap.peek())/2;
        } else if(minSize < maxSize){
            median= maxHeap.peek();
        }else {
            median= minHeap.peek();
        }
        return median;
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */