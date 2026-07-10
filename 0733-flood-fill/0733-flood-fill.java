class Solution {

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        // for(int r =0; r< image.length; r++){
        //     for(int c =0; c< image[r].length; c++){
                // if(r == sr && c == sc){
                    int originalColor = image[sr][sc];
                    dfs( image,sr,sc,originalColor, color, new boolean[ image.length][image[0].length]) ;
                // }
        //     }
        // }
       return image;
        
    }

    public void dfs(int[][] image,int r,int c, int originalColor,int color,boolean[][] visted){
        if(r < 0 || c< 0||  r>= image.length || c >= image[0].length){
            return ;
        }
        if(image[r][c] != originalColor ) return ;

        if(image[r][c] != color){
            image[r][c] = color;
            // visted[r][c]=true; 
            dfs(image,r,c+1,originalColor,color,visted);
            dfs(image,r,c-1,originalColor,color,visted);
            dfs(image,r+1,c,originalColor,color,visted);
            dfs(image,r-1,c,originalColor,color,visted);
        }


        
    }

}