class Solution {
    public boolean isValidSudoku(char[][] board) {

        // rows 
        Set<Character> hs=new HashSet<>();
        for(int i=0; i < board.length; i++ ){
            for(int j=0; j < board[i].length; j++ ){

                if(board[i][j] != '.') { 
                    if(hs.contains(board[i][j])){
                        return false;
                    }
                    hs.add(board[i][j]);
                }
                
                // int val=0;
                // if(board[i][j] != '.') { 
                //   val = Integer.parseInt(""+board[i][j]);
                // } else {
                //     // break;
                //     // exit here
                // }

                // if( board[i][j] != '.' && ( hs.contains(val) ||  val > 9  || val < 1 ) ){
                //     return false;
                // }
                // if(board[i][j] != '.') { 
                //     hs.add(val);
                // }


            }
            hs.clear();
        }

        for(int i=0; i < board.length; i++ ){
            for(int j=0; j < board[i].length; j++ ){

                if(board[j][i] != '.') { 
                    if(hs.contains(board[j][i])){
                        return false;
                    }
                    hs.add(board[j][i]);
                }

                //  int val=0;
                // if(board[j][i] != '.') { 
                //   val = Integer.parseInt(""+board[j][i]);
                // } else {
                //     // break;
                //     // exit here
                // }

                // if( board[j][i] != '.' && ( hs.contains(val) ||  val > 9  || val < 1 ) ){
                //     return false;
                // }
                // if(board[j][i] != '.') { 
                //     hs.add(val);
                // }
            }
            hs.clear();

        }


            // 00,01,02  10,11,12
            for (int row = 0; row < 9; row += 3) {

                for (int col = 0; col < 9; col += 3) {

                    hs.clear();

                    for (int i = row; i < row + 3; i++) {

                        for (int j = col; j < col + 3; j++) {

                            // validate board[i][j]
                            if(board[j][i] != '.') { 
                                if(hs.contains(board[j][i])){
                                    return false;
                                }
                                hs.add(board[j][i]);
                            }

                        }
                    }
                }
            }
        return true;
        
    }
}