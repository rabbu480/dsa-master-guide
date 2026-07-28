class Solution {

    TrieNode root;
    
    Solution(){
        root= new TrieNode();
    }
    class TrieNode{
        TrieNode[] children = new TrieNode[26];
        boolean isEnd=false;
        String encodedWord;
    }

    int sum =0;
    public int minimumLengthEncoding(String[] words) {
        root= new TrieNode();
        // TrieNode 
        // insert into try node  when end if value is -1 update anything elsedo not 
        // so our trie root has time val 5 bell val 5 so sum it by dfs 
        for(String word: words){
            insert(word);
        }
        dfs(root);
        return sum;

    }


    public void dfs(TrieNode node){

        if(node == null){
            return ;
        }

        boolean isLeaf = true;

        for (TrieNode child : node.children) {
            if (child != null) {
                isLeaf = false;
                break;
            }
        }
            // System.out.println(">>> >>>"+node.children);

            if(isLeaf &&  node.isEnd){

            System.out.println(">>> hh>>>"+node.encodedWord);  
            sum =sum+ node.encodedWord.length();
            } 

        for(TrieNode child: node.children){
 
            dfs(child);
        }

    }

    public void insert(String word){
        TrieNode curr=root;
        for(int i=word.length()-1; i >= 0 ; i--){
        // for(char c: word.toCharArray()){
            int index=word.charAt(i)-'a';
            if(curr.children[index] == null ){
                curr.children[index] = new TrieNode();
            }
            curr=curr.children[index];
        }
        curr.isEnd=true;
        curr.encodedWord=word+"#";
    }
}