# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        current_ptr = root 
        while stack or current_ptr:
            if current_ptr:
                stack.append(current_ptr)
                current_ptr = current_ptr.left
            else:
                current_ptr = stack.pop()
                result.append(current_ptr.val)
                current_ptr = current_ptr.right
        return result