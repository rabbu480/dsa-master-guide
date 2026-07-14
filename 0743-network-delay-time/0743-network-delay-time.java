class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // initlize adjcentList with the weights
        List<List<int[]>> adjWeightList= new ArrayList<>();
        for(int i=0; i<=n;i++){
            adjWeightList.add(new ArrayList<int[]>());
        }
        // mapthe the adjecents 
        for(int[] weightedNode : times){
           int from=weightedNode[0];
           int to=weightedNode[1];
           int time=weightedNode[2];
           // one directional 
           adjWeightList.get(from).add(new int[]{to,time}); 
        }
        // verify here 
    //    for (int i = 1; i < adjWeightList.size(); i++) {
    //         System.out.print(i + " -> ");
    //         for (int[] edge : adjWeightList.get(i)) {
    //             System.out.print(Arrays.toString(edge) + " ");
    //         }
    //         System.out.println();
    //     }

        // define the timeArray 
        int[] timedArray= new int[n+1];
        for(int i=0; i <= n ;i++){
            if(i!=k){
               timedArray[i]=Integer.MAX_VALUE;
            }
        }   
        System.out.print("\n"+Arrays.toString(timedArray) + " ");
        
        PriorityQueue<int[]> pq= new PriorityQueue<>( (a,b) -> a[1]-b[1] );
        pq.offer(new int[] {k,0});

        while(!pq.isEmpty()){
            int[] toWeightedNode= pq.poll();

            int to=toWeightedNode[0];
            int currentTime= toWeightedNode[1];
            if(currentTime > timedArray[to]){
                continue;
            }
            // (node, shortest distance from SOURCE)
            List<int[]> nextNodes= adjWeightList.get(to);
            for(int[] nextNode: nextNodes){
                int next=nextNode[0];
                int nextTime= nextNode[1];
                if(currentTime+nextTime < timedArray[next]){
                    timedArray[next]=currentTime+nextTime;
                    pq.offer(new int[]{next,currentTime+nextTime});
                }
            }

        }
        System.out.println("pq"+pq);
        int max = 0;

        for(int i = 1; i <= n; i++){

            if(timedArray[i] == Integer.MAX_VALUE){
                return -1;
            }

            max = Math.max(max, timedArray[i]);
        }

        return max;

        
    }
}