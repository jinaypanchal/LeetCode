class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        #dp[i] = True - means poch skta hu
        #dp[i] = False - filhaal naii poch skta hu
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if dp[j]  and (j + nums[j] >= i):
                    dp[i] = True
                    break
        
        return dp[n-1]


        # memo = {}
        # def f(idx):
        #     if idx in memo:
        #         return  memo[idx]

        #     if idx == n-1:
        #         return True
            
        #     if idx >= n:
        #         return False
            
        #     for i in range(1, nums[idx] + 1):
        #         if f(idx + i):
        #             memo[idx] = True
        #             return memo[idx]
            
        #     memo[idx] = False
        #     return memo[idx]
        
        # return f(0)


        