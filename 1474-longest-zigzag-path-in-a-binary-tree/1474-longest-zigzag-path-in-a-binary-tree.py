# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.maxi = 0
    
    # def f(self,node, steps, goleft):
    #     self.maxi = max(self.maxi, steps)

    #     if not node:
    #         return

    #     if goleft:
    #         self.f(node.left, steps + 1, False)
    #         self.f(node.right, 1, True)
    #     else:
    #         self.f(node.right, steps + 1, True)
    #         self.f(node.left, 1, False)  

    def longestZigZag(self, root: Optional[TreeNode]) -> int:  
        maxi = 0  
        def f(node, left, right):
            nonlocal maxi
            if not node:
                return 0

            maxi = max(maxi, left, right)
            f(node.left, right + 1, 0)
            f(node.right, 0, left + 1)

        f(root, 0 ,0)
        return maxi
        