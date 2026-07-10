class Solution {
    public void solve(char[][] board) {

        int rows = board.length;
        int cols = board[0].length;
        // get the protected in board
        for(int r =0 ; r< rows;r++) {
            // row on column first and last i.e board[0].length-1
            // if(board[r][0] == 'O'){
                dfs(board,r,0);
            // }
            // if(board[r][c] == 'O'){
                dfs(board,r,cols-1);
            // }
        }
        for(int c =0 ;c< cols;c++) {
            // column on first and last row  board[0].length-1
            // if(board[0][c] == 'O'){
                dfs(board,0,c);
            // }
            // if(board[rows][c] == 'O'){
                dfs(board,rows-1,c) ;
            // }
        }
        // make everything else except protected once in board.
        // System.out.println("board >>>" + Arrays.toString(board[0] ) );
        // System.out.println("board >>>" + Arrays.toString(board[board[0].length-1] ) );
        for(int r =0 ;r< board.length;r++) {
            for(int c =0 ; c< board[0].length;c++) {

                if(board[r][c] == 'O'){
                    board[r][c] = 'X' ;
                }
                if(board[r][c] == 'T'){
                    board[r][c] = 'O' ;
                }  

            }
        }
        // System.out.println("board >>>" + Arrays.toString(board ) );
        // for(int r =0 ;r< board.length;r++) {
        //     for(int c =0 ; c< board[0].length;c++) {

        //         // if(board[r][c] == 'O'){
        //         //     board[r][c] = 'X' ;
        //         // }
        //         if(board[r][c] == 'T'){
        //             board[r][c] = 'O' ;
        //         }  

        //     }
        // }

        // return board;
    }

    public void dfs(char[][] board,int r, int c){
        if(r<0 || c < 0|| r>=board.length || c>= board[0].length ){
            return;
        }
        System.out.println("board>>ooo" + board[r][c]  );
        // mark as protected 
        if(board[r][c] == 'O'){
            System.out.println("board>>ooo" + board[r][c]  );
            board[r][c] = 'T';
            
            dfs(board,r,c+1); 
            dfs(board,r,c-1);
            dfs(board,r-1,c);
            dfs(board,r+1,c);
            
        }
    }
}