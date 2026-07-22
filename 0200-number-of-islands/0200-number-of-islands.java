class Solution {
    public int numIslands(char[][] grid) {
        int count=0;
        for(int r=0;r< grid.length;r++) {
            for(int c=0;c< grid[0].length; c++) {

                if(grid[r][c] == '1'){
                    // from here search the island 
                    count++;
                    System.out.println("Bro >>>> "+"r : "+r+" c : "+c+" grid : "+grid[r][c]);
                    dfs(grid,r,c);
                    System.out.println("Done Bro >>>> "+"r : "+r+" c : "+c+" grid : "+grid[r][c]);
                }
            }   
        }

        return count;
    }
    public void dfs(char[][] grid,int r,int c) {
        
        // outside grid
        if( r < 0 || c < 0 || r >= grid.length || c >= grid[0].length ){
            return ;
        }

        System.out.println("r : "+r+" c : "+c+" grid : "+grid[r][c]);
        // water
        if(grid[r][c] == '0'){
            return;
        }
        int[][] directions={{0,1},{0,-1},{1,0},{-1,0}};
        // mark visited
        grid[r][c] = '0';
        for(int[] direction: directions){
            dfs(grid,r+direction[0],c+direction[1]);
        }

        // dfs(grid,r,c+1);
        // dfs(grid,r,c-1);
        // dfs(grid,r+1,c);
        // dfs(grid,r-1,c);

    }
}