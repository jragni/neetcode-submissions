# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 

        def _get_depth(node):
            if not node:
                return 0
            
            return 1 + max(_get_depth(node.left), _get_depth(node.right))
        
        if abs(_get_depth(root.left) - _get_depth(root.right)) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        