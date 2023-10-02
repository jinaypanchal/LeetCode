"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        final = []
        queue = [root]

        while queue:
            node_vals = []
            next_level = []
            for node in queue:
                node_vals.append(node.val)     

                if node.children:
                    next_level.extend(node.children)
            
            final.append(node_vals)
            queue = next_level
        
        return final
        