/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    inorderTraversal(root) {
        const inOrder = [];
        const _dfs = (node) => {
            if (!node) return 
            _dfs(node.left);
            inOrder.push(node.val);
            _dfs(node.right);
        }
        _dfs(root);
        return inOrder;
    }
}
