# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxi = 0
        
        def t(node):
            nonlocal maxi
            if not node:
                return 0
            
            l = t(node.left)
            r  = t(node.right)
            
            maxi = max(maxi, l+r)
            
            return max(l, r) + 1
        t(root)
        return maxi
        
                
