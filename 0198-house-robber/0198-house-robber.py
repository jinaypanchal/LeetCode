class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        
        def f(idx):
            if idx >= len(nums):
                return 0
            
            if idx in memo:
                return memo[idx]
            
            take_i = nums[idx] + f(idx + 2)
            skip_i = f(idx+1)

            memo[idx] = max(take_i, skip_i)
            return memo[idx]
        
        return f(0)