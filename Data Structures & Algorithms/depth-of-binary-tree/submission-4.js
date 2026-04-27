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
     * @return {number}
     */
    maxDepth(root) {

        const _dfs = (root, depth=1) => {
            if (!root) return depth - 1;

            return Math.max(
                _dfs(root.left, depth+1),
                _dfs(root.right, depth+1)
            );
        }
        return _dfs(root, 1);
    }
}
