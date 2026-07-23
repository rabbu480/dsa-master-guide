class WordDictionary {

    TrieNode root;

    public WordDictionary() {
        root=new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode current=root;
        // word=word.toLowerCase();
        for(char c: word.toCharArray()){
            int index=c-'a';
            if(current.childrens[index] ==  null){
                current.childrens[index]=new TrieNode();
            }
            current=current.childrens[index];
        }
        current.isEnd=true;         
    }


    
    public boolean search(String word) {
        // here we are not aware we have a root from root which node so lets travese
        return dfs( word,0,root);
        // word=word.toLowerCase();
        // TrieNode current=root;
        // for(char c: word.toCharArray()){
            
        //     int index=c-'a';
        //     // if(){
        //     //     current=current.childrens[index];
        //     // }

        //     if(-1<index && index < 27 && current.childrens[index] ==  null ){
        //         return false;
        //     }
        //     if(-1<index && index < 27){
        //         current=current.childrens[index];
        //     }
            
        // }
        // return current.isEnd;
    }

    public boolean dfs(String word,int i, TrieNode node){
        if(i==word.length()){
            return node.isEnd;
        }
        char c = word.charAt(i);
        // .
        if(c=='.'){
            // we need check from all the roots
            for( TrieNode child : node.childrens){
                if(child != null ){
                    if(dfs(word,i+1,child)){
                        return true;
                    }
                }
            }
            return false;
        }
        int index= c -'a';
        if(node.childrens[index] == null){
            return false;
        }
        return dfs(word,i+1,node.childrens[index]);
    }
}

// class Trie{
//     TrieNode=
// }
class TrieNode{
    TrieNode[] childrens = new TrieNode[26];
    boolean isEnd=false;
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */