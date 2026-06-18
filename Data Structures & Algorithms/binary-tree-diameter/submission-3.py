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

        def get_max_height(node):
            if not node:
                return 0
            return 1 + max(get_max_height(node.left), get_max_height(node.right))

        left = get_max_height(root.left)
        right = get_max_height(root.right)
        largest = left + right

        return max(largest, self.diameterOfBinaryTree(root.left) + self.diameterOfBinaryTree(root.right))
