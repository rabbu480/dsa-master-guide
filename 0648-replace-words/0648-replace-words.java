class Solution {

    TrieNode root;
    Solution(){
        root= new TrieNode();
    }
    public String replaceWords(List<String> dictionary, String sentence) {

        for(String dict: dictionary){
            insert(dict);
        }
        StringBuffer sb = new StringBuffer();
        String[] sentences=sentence.split(" ");
        for(int i =0 ; i< sentences.length ; i++){
            sb.append(checkPrefix(sentences[i]));
            if(i!=sentences.length-1){
                sb.append(" ");
            }
        }
        // insert the tries in dictionary
        // then check prefix in the triees again each sentance
        // append via string builder
        
        return new String(sb);
    }


    public String checkPrefix(String word){
        TrieNode curr=root;
        StringBuilder prefix = new StringBuilder();
        for(char c: word.toCharArray()){
            int index=c-'a';
            if(curr.childrens[index] == null){
                return word;
                // curr=curr.childrens[index] ;
            }
            curr=curr.childrens[index] ;
            prefix.append(c);
            if(curr.isEnd){
                return prefix.toString();
            }
        }

        return word;
    }

    public void insert(String Word){
        TrieNode curr=root;
        for(char c: Word.toCharArray()){
            int index=c-'a';
            if(curr.childrens[index] == null){
                curr.childrens[index] = new TrieNode();

                // curr=curr.childrens[index] ;
            }
            curr=curr.childrens[index];
        }
        curr.isEnd=true;

    }
}

class TrieNode{
    TrieNode[] childrens= new TrieNode[26];
    boolean isEnd=false;
}