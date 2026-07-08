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
    public boolean isBalanced(TreeNode root) {
        if(root == null ) return true;
        int left=maxDepth(root.left);
        int right=maxDepth(root.right);
        // System.out.println("left::"+left +" right ::" + right );
        // current node balanced?
        boolean currentBalanced =
            Math.abs(left - right) <= 1;
        return currentBalanced && isBalanced(root.left)
            && isBalanced(root.right);
    }

    int maxDepth(TreeNode root){
        if(root == null ) return 0;
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        // System.out.println("left::"+left +" right ::" + right );
        return  Math.max(left,right)+1;       
    }

}