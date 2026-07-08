/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {


        Queue<TreeNode> queue= new LinkedList<>();
        List<List<Integer>> levels= new ArrayList<>();
        // CHeck root is null treeNode it slef empty.
        if(root == null){
            return levels;
        }
        queue.offer(root);
        // iterate queue level by level until all level covred.
        while(!queue.isEmpty()){

            int size=queue.size();
            List<Integer> level= new ArrayList<>();
            // get top element of queue remove that add it chailds so it contains only current level add remove level, 
            // remove current level from queue, add to list, add next level to queue 
            for(int i=0;i< size;i++){
                TreeNode node=queue.poll();
                level.add(node.val);
                if(node.left != null) queue.offer(node.left);
                if(node.right != null) queue.offer(node.right);
            }
            levels.add(level);
        }
        return levels;
    }
}