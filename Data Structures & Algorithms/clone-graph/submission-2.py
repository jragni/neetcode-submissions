"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node'], visited=set()) -> Optional['Node']:
        if not node:
            return node

        visited = {}
        def dfs(n):
            if n.val in visited:
                return visited[n.val]
            
            res = Node(val=n.val, neighbors=[]) 
            visited[n.val] = res
            for neighbor in n.neighbors:
                res.neighbors.append(dfs(neighbor))
            
            return res
        
        return dfs(node)

            