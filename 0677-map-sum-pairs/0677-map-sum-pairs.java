class MapSum {

    TrieNode root;

    public MapSum() {
        root= new TrieNode();
    }
    
    public int sum(String prefix) {
        int sum=0;
        TrieNode curr=root;
        System.out.println("curr >> "+curr);
        for(char ch: prefix.toCharArray()){
            int index= ch-'a';
            if(curr.children[index] == null){
               return 0;
            }
            curr=curr.children[index];
            System.out.println("index::"+index+" curr:"+curr.val );
        }
        return dfs(curr); // from prix do dfs to get sum 
    }

        private int dfs(TrieNode node) {

            if (node == null)
                return 0;

            int sum = 0;

            if (node.isEnd)
                sum += node.val;

            for (TrieNode child : node.children) {
                sum += dfs(child);
            }

            return sum;
        }

    public void insert(String key, int val) {
        TrieNode curr=root;
        for(char ch: key.toCharArray()){
            int index= ch-'a';
            if(curr.children[index] == null){
               curr.children[index] = new TrieNode();
            }
            curr=curr.children[index];
        }
        curr.isEnd=true;
        curr.val=val;
        System.out.println("curr >> "+curr);
    }

    
}

class TrieNode{
    TrieNode[] children;
    Boolean isEnd=false;
    int val =-1;

    public TrieNode(){
        this.children=new TrieNode[26];
        this.val=-1;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        sb.append("TrieNode{");
        sb.append("isEnd=").append(isEnd);
        sb.append(", val=").append(val);
        sb.append(", children=[");

        for (int i = 0; i < 26; i++) {
            if (children[i] != null) {
                sb.append((char) ('a' + i)).append(" ");
            }
        }

        sb.append("]}");
        return sb.toString();
    }


    

}


// class MapSum {

//     class TrieNode {
//         TrieNode[] children = new TrieNode[26];
//         int sum = 0;
//     }

//     TrieNode root;
//     Map<String, Integer> map;

//     public MapSum() {
//         root = new TrieNode();
//         map = new HashMap<>();
//     }

//     public void insert(String key, int val) {

//         int oldValue = map.getOrDefault(key, 0);
//         int delta = val - oldValue;

//         map.put(key, val);

//         TrieNode curr = root;

//         for (char ch : key.toCharArray()) {

//             int index = ch - 'a';

//             if (curr.children[index] == null) {
//                 curr.children[index] = new TrieNode();
//             }

//             curr = curr.children[index];
//             curr.sum += delta;
//         }
//     }

//     public int sum(String prefix) {

//         TrieNode curr = root;

//         for (char ch : prefix.toCharArray()) {

//             int index = ch - 'a';

//             if (curr.children[index] == null) {
//                 return 0;
//             }

//             curr = curr.children[index];
//         }

//         return curr.sum;
//     }
// }
/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */