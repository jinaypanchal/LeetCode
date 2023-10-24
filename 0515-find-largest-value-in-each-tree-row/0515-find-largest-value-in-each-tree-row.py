# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = [root]
        res = []
        while queue:
            temp = []
            next_level = []
            for node in queue:
                temp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            res.append(max(temp))
            queue = next_level
        
        return res

        # if not root:
        #     return []
        
        # queue = [root]
        # res = []
        # while queue:
        #     temp = []
        #     next_level = []
        #     for node in queue:
        #         temp.append(node.val)
        #         if node.left:
        #             next_level.append(node.left)
        #         if node.right:
        #             next_level.append(node.right)
            
        #     res.append(max(temp))
        #     queue = next_level
        
        # return res
        

            