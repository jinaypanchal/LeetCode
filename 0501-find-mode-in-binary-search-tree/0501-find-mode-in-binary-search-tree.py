# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # if root == [0]:
        #     return [0]

        d = {}
        def inorder(node):
            if not node:
                return []
            
            inorder(node.left)
            if node.val not in d:
                d[node.val] = 1
            else:
                d[node.val] += 1
            inorder(node.right)
        inorder(root)
        # print(d)
        sorted_dict = dict(sorted(d.items(), key = lambda x:x[1]))
        print(sorted_dict)
        res = []
        maxi = max(sorted_dict.values())
        for key,val in sorted_dict.items():
            if val == maxi:
                res.append(key)
        
        return res


        #  res = []
        #  for key, val in sorted_dict.items():
        #      if 
        

