# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def _get_max_depth(n):
            if not n:
                return 0
            return 1 + max(_get_max_depth(n.left), _get_max_depth(n.right))

        left_depth = _get_max_depth(root.left)
        right_depth = _get_max_depth(root.right)

        diameter = left_depth + right_depth
        subtree_diameter = max(
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right))

        return max(diameter, subtree_diameter)