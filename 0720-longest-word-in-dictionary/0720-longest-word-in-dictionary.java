class Solution {

    TrieNode root;

    class TrieNode{
        TrieNode[] children= new TrieNode[26];
        String word;
        boolean isEnd = false;
    }

    Solution(){
        root= new TrieNode();
    }

    String longestWord="";
    public String longestWord(String[] words) {

        for(String word : words){
           insert(word); 
        }
        dfs(root);
        return longestWord;
        
    }


    private void dfs(TrieNode node) {
        // 1. Update answer if needed

        // 2. For every child from a-z

                // child != null

                // child.isWord

                // dfs(child) 

        for(TrieNode child : node.children){
            if(child != null && child.isEnd) {
                if(longestWord.length() < child.word.length()){
                    longestWord= child.word;
                }
                dfs(child); 
            }
        }

            
    }

    public void insert(String word) {
        TrieNode curr=root;
        
        for(char c: word.toCharArray()){
            int index =c-'a';
            if(curr.children[index] == null){
                curr.children[index]=new TrieNode();
            }
            curr=curr.children[index];
        }
        curr.isEnd = true;
        curr.word = word;
    }

}