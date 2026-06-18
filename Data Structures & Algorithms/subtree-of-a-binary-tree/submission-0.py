# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and subRoot:
            return False
        if root and not subRoot:
            return True
        
        def is_same_tree(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (not node1 and node2):
                return False
            if node1.val != node2.val:
                return False
            
            return is_same_tree(node1.left, node2.left) and is_same_tree(node1.right, node2.right)
        
        if root.val == subRoot.val and is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
