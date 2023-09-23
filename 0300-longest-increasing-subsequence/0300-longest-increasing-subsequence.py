class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if not nums:
            return 0
        
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
        # memo = {}

        # def f(curr_i, prev):
        #     if curr_i >= n:
        #         return 0
            
        #     if (curr_i, prev) in memo:
        #         return memo[(curr_i, prev)]
           
        #     take = 0
        #     if prev == -1 or nums[curr_i] > nums[prev]:
        #         take = 1 + f(curr_i + 1, curr_i)
            
        #     skip = f(curr_i + 1, prev)
        #     # return max(take, skip)
        #     memo[(curr_i, prev)] = max(take, skip)

        #     return memo[(curr_i, prev)]

        # max_length = 0
        # for i in range(n):
        #     max_length = max(max_length, f(i,-1))

        # return max_length
        