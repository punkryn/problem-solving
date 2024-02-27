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
    private int ans = 0;
    public int longestUnivaluePath(TreeNode root) {
        if (root == null) return 0;
        dfs(root, root.val);
        return ans;
    }

    private int dfs(TreeNode cur, int prev) {
        if (cur == null) return 0;
        int left = dfs(cur.left, cur.val);
        int right = dfs(cur.right, cur.val);

        ans = Math.max(ans, left + right);
        if (cur.val == prev) return Math.max(left, right) + 1;
        return 0;
    }
}