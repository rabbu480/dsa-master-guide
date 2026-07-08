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

    // kth smallest 
    int smallestVal=-1;
    public int kthSmallest(TreeNode root, int k) {
        dfs(root,k);
        return smallestVal;
    }

    // BST is already sorted order for in order
    int count=0;
    public void dfs(TreeNode root,int k){
        if(root == null ) return;
        // in order 
        dfs(root.left,k);
        count++;
        if(count==k) {
            smallestVal= root.val;
        } 
        dfs(root.right,k);

        // return 0;
    }
}