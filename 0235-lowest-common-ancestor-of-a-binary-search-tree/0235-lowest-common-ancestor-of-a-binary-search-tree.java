/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
               // if(root == null) return root;
        if(root == null) return null;

        // p and q both less than root then left side  
        if(p.val < root.val && q.val < root.val) {
            return lowestCommonAncestor(root.left,p,q);
        }
        // p and q both less than root then right side 
        if(p.val > root.val && q.val > root.val) {
            return lowestCommonAncestor(root.right,p,q);
        }
        // as we itrating from top so if we found condition left<root < right then valid and the root the lca
        return root;
        
        
    }
    
}