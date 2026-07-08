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
    // this is O(n2) avoid.
    // public boolean isBalanced(TreeNode root) {
    //     if(root == null ) return true;
    //     int left=maxDepth(root.left);
    //     int right=maxDepth(root.right);
    //     // System.out.println("left::"+left +" right ::" + right );
    //     // current node balanced?
    //     boolean currentBalanced =
    //         Math.abs(left - right) <= 1;
    //     return currentBalanced && isBalanced(root.left)
    //         && isBalanced(root.right);
    // }

    // int maxDepth(TreeNode root){
    //     if(root == null ) return 0;
    //     int left = maxDepth(root.left);
    //     int right = maxDepth(root.right);
    //     // System.out.println("left::"+left +" right ::" + right );
    //     return  Math.max(left,right)+1;       
    // }

    boolean isBalnced=true;
    public boolean isBalanced(TreeNode root) {

        // 1
        // /\
        // 2 2
        // /  \
        // 3  3
        // /   \
        // 4    4

        if(root == null){
            return true;
        }

        maxDepth( root);
        return isBalnced;
    }

    public int maxDepth(TreeNode root){
        if(root == null) return 0;
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        // each node from root checkif this balanced or not 
        if(Math.abs(left-right) > 1 ) {
            isBalnced= false;
            return -1;
        }        
        return 1+ Math.max(left,right);
    }

}