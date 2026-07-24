class Solution {
    TrieNode root;

    Solution(){
        root=new TrieNode();
    }

    ArrayList result= new ArrayList();

    public List<String> findWords(char[][] board, String[] words) {
        
        // Build Trie
        for(String word: words){
            insert(word);
        }


        // List<String> al = new ArrayList<>();
        // Start DFS from every cell
        for(int r=0; r< board.length; r++){
            for(int c=0; c< board[0].length; c++){
                dfs(board,r,c,root);
            }
        }
        // Keep all the words in trieNode
        // do dfs acorss the check if we can get end 
        // dfs(board,0,0,Tries)
        return result;
    }
    
    void dfs(char[][] board,int r,int c,TrieNode node){
        // TrieNode current=node;
        if(r<0 || c<0 || r>= board.length  || c >= board[0].length){
            return ;
        }
        // Already visited
        char ch = board[r][c];

        if (ch == '#')  return;

         int index = ch - 'a';

        // Prefix doesn't exist
        if (node.children[index] == null) return;

        node = node.children[index];

        // Word found
        if (node.word != null) {
            result.add(node.word);
            // Avoid duplicates
            node.word = null;
        }

        // Mark visited
        board[r][c] = '#';

        int[][] DIR={{0,1},{0,-1},{1,0},{-1,0}};
        for(int[] d:DIR){
            int dr=d[0];
            int dc=d[1];
            dfs(board,r+dr,c+dc,node);
        }
        // Backtrack
        board[r][c] = ch;
    }

    void insert(String word){
        TrieNode curr= root;
        for(char c:word.toCharArray()){
            int index=c-'a';
            if(curr.children[index] == null){
                curr.children[index]=new TrieNode();
            }
            curr=curr.children[index];
        }
        curr.word=word;  // Stores complete word if this node is end
        
    }
}

class TrieNode{
    TrieNode[] children=new TrieNode[26];
    boolean isEnd;
    String word; // Stores complete word if this node is end
}