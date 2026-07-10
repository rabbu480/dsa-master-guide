class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {

        List<List<Integer>> graph = buildGraph(edges,n);
        // 0 -> 1,2
        // 1 -> 0,2
        // 2 -> 0,1
        System.out.println(graph);
        boolean[] visted= new boolean[n];
        return hasValidPath(source,destination,graph,visted);
        
        
    }

    public boolean hasValidPath(int current, int destination,List<List<Integer>> graph,boolean[] visted){

        List<Integer> neghbors=graph.get(current);
        
        if(current == destination){
            return true;
        }
        visted[current]= true;
        for(int neghbor: neghbors){
            if(!visted[neghbor]  ){
                if(hasValidPath(neghbor,destination,graph,visted)){
                return true;
                }

            }
            
        }
        return false;
    }


    
    public List<List<Integer>>buildGraph(int[][] edges,int n ){
        List<List<Integer>> graph= new ArrayList<>();
        for(int i=0;i< n ; i++){
           graph.add(new ArrayList()); 
        }

        for(int[] edge: edges){
            int u = edge[0];
            int v = edge[1];
            graph.get(u).add(v);
            graph.get(v).add(u);
        }

        return graph ;
    }
}