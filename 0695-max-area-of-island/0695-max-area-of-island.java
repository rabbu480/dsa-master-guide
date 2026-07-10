class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int maxAreaOfIsland=0;
        for(int r=0 ; r< grid.length; r++){
            for(int c=0; c< grid[r].length ; c++ ){
                if(grid[r][c] == 1) {
                    int areaOfIsland = dfsIlandArea(grid,r,c);
                    System.out.println("r: "+r +" c: " +c +"areaOfIsland: "+areaOfIsland);
                    maxAreaOfIsland=Math.max(maxAreaOfIsland,areaOfIsland);
                }
            }
        }
        return maxAreaOfIsland;
        
    }

    public int dfsIlandArea(int [][] grid,int r,int c) {
        if(r<0 || c<0 || r>= grid.length || c>= grid[0].length) {
            return 0;
        }
        if(grid[r][c] == 0 ) return 0;
        grid[r][c] = 0 ;

        return 1+ dfsIlandArea(grid,r,c+1) 
                +dfsIlandArea(grid,r,c-1)
                +dfsIlandArea(grid,r+1,c)
                +dfsIlandArea(grid,r-1,c);   

    }

}