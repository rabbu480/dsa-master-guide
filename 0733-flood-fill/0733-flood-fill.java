class Solution {

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        // for(int r =0; r< image.length; r++){
        //     for(int c =0; c< image[r].length; c++){
                // if(r == sr && c == sc){
                    int originalColor = image[sr][sc];
                    dfs( image,sr,sc,originalColor, color) ;
                    System.out.println("originalColor: " +originalColor +" color : "+color);
                // }
        //     }
        // }
       return image;
        
    }

    public void dfs(int[][] image,int r,int c, int originalColor,int newColor){
        if(r < 0 || c< 0||  r>= image.length || c >= image[0].length){
            return ;
        }
        // originalColor=1,1 no return ==> 1 and 2
        // originalColor=1,1 no return ==> 1 and 2
        // 2 != 1;
        // 
        if(image[r][c] != originalColor ) return ;
        // if this orignal only comes here then we know it orginal why we check ing 
        if(image[r][c] != newColor){
            image[r][c] = newColor;
            dfs(image,r,c+1,originalColor,newColor);
            dfs(image,r,c-1,originalColor,newColor);
            dfs(image,r+1,c,originalColor,newColor);
            dfs(image,r-1,c,originalColor,newColor);
        }


        
    }

}