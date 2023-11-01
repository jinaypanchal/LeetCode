# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            nonlocal maxi, prev, ct, mode
            if not node:
                return
                        
            inorder(node.left)            
            if node.val == prev:
                ct += 1
            else:
                ct = 1
            
            if ct > maxi:
                maxi = ct
                mode = [node.val]
            elif ct == maxi:
                mode.append(node.val)
            
            prev = node.val
            inorder(node.right)      
        
        
        maxi = 0
        prev = None
        ct = 0
        mode = []
        inorder(root)
        return mode
            



        # # if root == [0]:
        # #     return [0]

        # d = {}
        # def inorder(node):
        #     if not node:
        #         return []
            
        #     inorder(node.left)
        #     if node.val not in d:
        #         d[node.val] = 1
        #     else:
        #         d[node.val] += 1
        #     inorder(node.right)
        # inorder(root)
        # # print(d)
        # sorted_dict = dict(sorted(d.items(), key = lambda x:x[1]))
        # print(sorted_dict)
        # res = []
        # maxi = max(sorted_dict.values())

        
        # for key,val in sorted_dict.items():
        #     if val == maxi:
        #         res.append(key)
        
        # return res


        # #  res = []
        # #  for key, val in sorted_dict.items():
        # #      if 
        

