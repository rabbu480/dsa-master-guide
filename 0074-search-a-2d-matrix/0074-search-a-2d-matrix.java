class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rRow=matrix.length;
        int rCol=matrix[0].length;
        // R0: 0 ,1 ,2 , 3   ==> 0x+c
        // R1: 4 ,5 ,6 , 7   ==> 4x+c
        // R2: 8 ,9 ,10, 11  ==> 4*2*x+c
        //     c0,c1,c2, c3
        // based on mid lets get r,c
        // mid=9 r=2 , c=1 
        int left=0;
        int right=rRow*rCol-1;
        while(left <= right){
            int mid=left+(right-left)/2;
            int row=mid/rCol;
            int col=mid%rCol;
            int midVal=matrix[row][col];
            if(midVal == target ){
                return true;
            } else if(midVal < target ){
                left=mid+1;
            } else {
                right=mid-1;
            }

        }
        return false;
    }
}