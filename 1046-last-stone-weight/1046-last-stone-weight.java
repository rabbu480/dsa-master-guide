class Solution {
    public int lastStoneWeight(int[] stones) {
        // populate into prioirty Queue
        // get the top 2  while queue is empty.
        // if x==y then destroy both peek then pop x & y 
        // if x<y then y= y=y-x
        PriorityQueue<Integer> pq= new PriorityQueue<>(Collections.reverseOrder());
        for(int stone:stones){
            pq.offer(stone);
        }
        //  System.out.println("---"+pq);
        while(pq.size() > 1){

            int y=pq.poll(); // heavysest 
            int x=pq.poll(); // next heavisest
            // ^^^smash 
            // 
            System.out.println("-xx--"+pq);
            if(x<y){
                pq.offer(y-x);
            }
        }


        return pq.isEmpty()?0:pq.peek();  
        
    }
}