class Solution {

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        // for(int r =0; r< image.length; r++){
        //     for(int c =0; c< image[r].length; c++){
                // if(r == sr && c == sc){
                    int val = image[sr][sc];
                    dfs( image,sr,sc,val, color, new boolean[ image.length][image[0].length]) ;
                // }
        //     }
        // }
       return image;
        
    }

    public void dfs(int[][] image,int r,int c, int val,int color,boolean[][] visted){
        if(r < 0 || c< 0||  r>= image.length || c >= image[0].length){
            return ;
        }
        if(image[r][c] != val ) return ;

        if(image[r][c] == val && image[r][c] != color){
            image[r][c] = color;
            // visted[r][c]=true; 
            dfs(image,r,c+1,val,color,visted);
            dfs(image,r,c-1,val,color,visted);
            dfs(image,r+1,c,val,color,visted);
            dfs(image,r-1,c,val,color,visted);
        }


        
    }

}