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

    // 
    int count=0;
    public void dfs(TreeNode root,int k){
        if(root == null ) return;
        dfs(root.left,k);
        // System.out.println(count);
        count++;
        // System.out.println(count);
        if(count==k) {
            System.out.println("root.val :: " +root.val);
            smallestVal= root.val;
            // return root.val;
        } 

        dfs(root.right,k);

        // return 0;
    }
}