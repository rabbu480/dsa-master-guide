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


    int diameter=0;
    public int diameterOfBinaryTree(TreeNode root) {
        maxDepth(root);
        return diameter;
    }
    public int maxDepth(TreeNode root){
        int left=0;
        int right=0;
        if(root == null) return 0;
        left=maxDepth(root.left);
        right=maxDepth(root.right);
        diameter=Math.max(diameter,left+right);
        return Math.max(left,right)+1;
    }
        
}