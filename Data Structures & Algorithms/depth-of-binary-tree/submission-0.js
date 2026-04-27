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
        let md = 0;
        if (!root) return md;

        const _helper = (root, count = 1) => {
            if (!root)  return count - 1;
            return 1 + Math.max(_helper(root.left), _helper(root.right));
        };
        return _helper(root);
    }
}
