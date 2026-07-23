class TrieNode{
    TrieNode[] childrens = new TrieNode[26];
    boolean isEnd=false;

}
class Trie {
    TrieNode root;
    public Trie() {
        root = new TrieNode();
    }
    
    public void insert(String word) {
        // assign cuurent to root.
        // loop each character get index of each char
        // check if the character not in trieNode then inser move current=current.childrens[index]
        TrieNode current=root;
        for(char c : word.toCharArray()){
            int index=c-'a';
            if(current.childrens[index] == null){
                current.childrens[index]=new TrieNode();
            }
            current=current.childrens[index];
        }
        current.isEnd=true;

    }
    
    public boolean search(String word) {
        // assign cuurent to root.
        // loop each character get index of each char
        // check if each character is already in the trienode if not then return false.
        TrieNode current=root;
        for(char c: word.toCharArray() ) {
            int index=c-'a';
            if(current.childrens[index] == null){
                return false;
            }
           current= current.childrens[index];
        }

        return current.isEnd;
        
    }
    
    public boolean startsWith(String prefix) {

        TrieNode current=root;
        for(char c: prefix.toCharArray() ) {
            int index=c-'a';
            if(current.childrens[index] == null){
                return false;
            }
           current = current.childrens[index];
        }

        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */