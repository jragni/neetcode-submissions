/**
 * // Definition for a Node.
 * class Node {
 *     constructor(val = 0, neighbors = []) {
 *       this.val = val;
 *       this.neighbors = neighbors;
 *     }
 * }
 */

class Solution {
    /**
     * @param {Node} node
     * @return {Node}
     */
    cloneGraph(node) {
        const copyMap = new Map();

        function _dfs(node) {
            if (!node) return null;
            if (copyMap.has(node)) return copyMap.get(node);

            const copy = new Node(node.val);

            copyMap.set(node, copy);

            for (const n of node.neighbors) {
                copy.neighbors.push(_dfs(n));
            }

            return copy;
        }

        return _dfs(node);
    }
}
