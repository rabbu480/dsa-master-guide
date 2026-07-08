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

        List<List<Integer>> result = new ArrayList();
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        if (root == null) {
            return result;
        }

        while (!queue.isEmpty()) {
            int size = queue.size();
            List childrens = new ArrayList();
            for (int i = 0; i < size; i++) {
                TreeNode tee = queue.poll();
                childrens.add(tee.val);
                if (tee.left != null) {
                    queue.offer(tee.left);
                }
                if (tee.right != null) {
                    queue.offer(tee.right);
                }
                 
            }
            result.add(childrens);
        }

        return result;
    }
}