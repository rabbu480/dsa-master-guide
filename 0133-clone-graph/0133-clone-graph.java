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
        printMap(clonedMap);
        // System.out.println("clonedMap:: " + clonedMap);
        // printNode(">> nodeCopy >>>",nodeCopy);
        if(node.neighbors != null ){
            // System.out.println("node.val:: " +node.val);
            for(Node nodez : node.neighbors){
                // here dfs return each negbors negbors
                // neighbors.add(nodeCopy);
                Node neighbor = dfs(nodez);
                //1 ==> 
                // 2
                // get related and add to it so now here 2 add relation 1
                // printNode(">>> neighbor >>>",neighbor);
                nodeCopy.neighbors.add(neighbor);
                // System.out.println("nodez.val::: " +nodeCopy);
            }
        }
        // printNode(">>> after >>>",nodeCopy);

        return nodeCopy;

    }

    private void printMap(Map<Node, Node> clonedMap) {

        System.out.println("\n========== Clone Map ==========");

        for (Map.Entry<Node, Node> entry : clonedMap.entrySet()) {

            System.out.println(
                "Original " + entry.getKey().val +
                " --> " +
                nodeToString(entry.getValue())
            );
        }

        System.out.println("================================\n");
    }

    private String nodeToString(Node node) {

        if (node == null) {
            return "null";
        }

        StringBuilder sb = new StringBuilder();

        sb.append("Clone ")
        .append(node.val)
        .append(" -> [ ");

        for (Node neighbor : node.neighbors) {
            sb.append(neighbor.val).append(" ");
        }

        sb.append("]");

        return sb.toString();
    }

    private void printNode(String prefix,Node node) {

        if (node == null) {
            System.out.println("null");
            return;
        }

        System.out.print(prefix+ " Node " + node.val + " -> [ ");

        for (Node neighbor : node.neighbors) {
            System.out.print(neighbor.val + " ");
        }

        System.out.println("]");
    }
}