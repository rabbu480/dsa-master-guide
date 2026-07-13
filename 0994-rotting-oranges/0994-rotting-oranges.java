class Solution { 
    public int orangesRotting(int[][] grid) {
        // Step 1: Add ALL rotten oranges to queue
        //         Count fresh oranges
         // No fresh oranges
        //          int[][] directions = {
        //     {0, 1},
        //     {0, -1},
        //     {1, 0},
        //     {-1, 0}
        // };

        // Step 1: Add ALL rotten oranges to queue
        //         Count fresh oranges

        Queue<int[]> queue= new LinkedList<>();
        int goodOranges=0;
        for(int r=0; r< grid.length ; r++){
            for(int c=0; c< grid[0].length ; c++){
                if(grid[r][c] == 2){
                    queue.offer(new int[]{r,c});
                }
                if(grid[r][c] == 1){
                    goodOranges++;
                }
            }
        }
        System.out.println("goodOranges:" +goodOranges);

        // boolean[][] visited = new boolean[grid.length][grid[0].length];
        int timer=0;
        while(!queue.isEmpty()){
            boolean spread = false;
            int [][] directions = { {0,1},{0,-1},{1,0},{-1,0}};
            int size = queue.size();
            for(int i =0; i <size ; i++){
                int[] current= queue.poll();
                for(int[] direction: directions  ){
                    int cr= current[0];
                    int cc= current[1];
                    int dr=direction[0] ;
                    int dc=direction[1] ;
                    int r=cr+dr;
                    int c=cc+dc;
                    if(c < 0 || r < 0 || c >=  grid[0].length || r>=  grid.length){
                        continue;
                    }
                    // if(visited[r][c]) continue;
                    if(grid[r][c] != 1) continue;
                    
                    // visited[r][c]=true;
                    goodOranges--;
                    spread = true;
                    queue.offer(new int[]{r,c});
                    grid[r][c] =2;
                }
            }
            // for each level we need check this 
            if(spread){
                // spread = false;
                timer=timer+1;
                
            }
        }
        System.out.println("grid::"+Arrays.deepToString(grid));
        System.out.println("timer::"+timer);
        if(goodOranges != 0) {
            return -1;
        } else {
            return timer;
        }

    }



}