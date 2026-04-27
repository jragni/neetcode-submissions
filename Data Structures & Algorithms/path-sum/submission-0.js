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
     * @param {number} targetSum
     * @return {boolean}
     */
    hasPathSum(root, targetSum) {
        const _helper = (node, sum=0) => {
            if (!node) return false;
            if (!node.left && !node.right) return sum === targetSum;
            const left = node.left ? node.left.val : 0;
            const right = node.right ? node.right.val : 0;
            return _helper(node.left, sum + left) || _helper(node.right, sum + right);
        }
        if (!root) return false;
        return _helper(root, root.val);
    }
}
