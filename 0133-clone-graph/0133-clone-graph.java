/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    Map<Node,Node> clonedMap= new HashMap();

    public Node cloneGraph(Node node) {
        return dfs(node);
    }

    public Node dfs(Node node){
        // check current node 
        // make current negbor as visted 
        // get all neigbors;
        if(node == null) return null;

        if(clonedMap.containsKey(node)){
            return clonedMap.get(node);
        }

        Node nodeCopy = new Node(node.val);
        clonedMap.put(node,nodeCopy);
        // System.out.println("clonedMap:: " + clonedMap);
        if(node.neighbors != null ){
            System.out.println("node.val:: " +node.val);
            for(Node nodez : node.neighbors){
                // here dfs return each negbors negbors
                // neighbors.add(nodeCopy);
                Node neighbor = dfs(nodez);
                //1 ==> 
                // 2
                // get related and add to it so now here 2 add relation 1
                nodeCopy.neighbors.add(neighbor);
                System.out.println("nodez.val::: " +nodeCopy);
            }
        }
        return nodeCopy;

    }
}