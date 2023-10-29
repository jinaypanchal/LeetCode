# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        t = []
        swap =[]
        def inorder(node):
            if not node:
                return []
            
            if node:
                inorder(node.left)
                t.append(node.val)
                inorder(node.right)               
        
        inorder(root)

        for i, j in zip(t, sorted(t)):
            if i!=j:
                swap.append(i)

        def inorderSwap(node):
            if not node:
                return []
            
            if node:
                inorderSwap(node.left)
                if node.val == swap[0]:
                    node.val = swap[1]
                elif node.val == swap[1]:
                    node.val = swap[0]
                # t.append(node.val)
                inorderSwap(node.right) 

        inorderSwap(root)
        return root
        """
        Do not return anything, modify root in-place instead.
        """
        