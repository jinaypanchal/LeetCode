# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def post(node):
            nonlocal res
            if not node:
                return [0, 0]
            
            leftlist = post(node.left)
            rightlist = post(node.right)
            sumi = node.val + leftlist[0] + rightlist[0]
            node_ct = leftlist[1] + rightlist[1] + 1
            if sumi // node_ct == node.val:
                res += 1
            
            return [sumi, node_ct]
        
        res = 0
        post(root)
        return res

        # ans = 0
        
        # stack = [(root, False, (0, 0), (0, 0))]
        # while stack:
        #     node, visited, left_result, right_result = stack.pop()
        #     if not node:
        #         continue
            
        #     if visited:
        #         leftSum, leftCount = left_result
        #         rightSum, rightCount = right_result
        #         summ = node.val + leftSum + rightSum
        #         count = 1 + leftCount + rightCount
        #         if summ // count == node.val:
        #             ans += 1
        #     else:
        #         stack.append((node, True, left_result, right_result))
        #         if node.right:
        #             stack.append((node.right, False, (0, 0), (0, 0)))
        #         if node.left:
        #             stack.append((node.left, False, (0, 0), (0, 0)))
        
        # return ans
