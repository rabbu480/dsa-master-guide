class Solution {
    public void solve(char[][] board) {
        // iterate all the edges anything in edge make it safe
        // all remaining Mark 'x'
        // i=0 || m    and j 0..n-1
        // i= 0,n j = 0 & m 
        // for(int i=0;i<n; i++){
        //     for(int j =0; j<n ; j++){
        //         dfs(i,j,board);
        //     }
        // }

        int m = board.length; // rows i m
        int n = board[0].length; //cols j n

        for(int j =0; j<n ; j++){
            if(board[0][j] == 'O') {    dfs(0,j,board);}
            if(board[m-1][j] == 'O') dfs(m-1,j,board); 
        }
        // for(int j =0; j<n ; j++){
        //     if(board[m-1][j] == 'O') dfs(m-1,j,board); 
        // }
        for(int i =0; i<m ; i++){
            if(board[i][0] == 'O') dfs(i,0,board);
            if(board[i][n-1] == 'O') dfs(i,n-1,board);
        }


        for(int i=0;i<m; i++){
            for(int j =0; j<n ; j++){
                if(board[i][j] == 'O') board[i][j] = 'X';
                if(board[i][j] == 'S') board[i][j] = 'O';
            }
        }


        
    }

    void dfs(int i,int j,char [][] board){

        int m = board.length;
        int n = board[0].length;

        if(i<0 || j<0 || i>=m ||  j >= n || board[i][j] != 'O') return ; 

        int[][] directions ={{0,1},{0,-1},{1,0},{-1,0}};

        if(board[i][j] == 'O' ) board[i][j] = 'S';

        for(int[] d: directions ) {
            dfs(i+d[0],j+d[1],board);
        }
    
    }
}