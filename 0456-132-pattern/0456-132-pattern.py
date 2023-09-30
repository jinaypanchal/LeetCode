class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        num3 = float('-inf')
        stack = []
        for i in range(n-1, -1, -1):
            if num3 > nums[i]:
                return True
            
            while stack and stack[-1] <  nums[i]:
                num3 = stack[-1]
                stack.pop()
            
            stack.append(nums[i])
        
        return False

        #CSWM
        #Better
        # num_i = nums[0]
        # for j in range(1,n-1):
        #     num_i = min (num_i, nums[j])
        #     for k in range(j+1, n):
        #         if num_i < nums[k] and nums[k] < nums[j]:
        #             return True
        
        # return False

        
        # Brute Approach
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if nums[i] < nums[j]:
        #             for k in range(j+1, n):
        #                 if nums[k] < nums[j] and nums[k] > nums[i]:
        #                     return True
        
        # return False
        