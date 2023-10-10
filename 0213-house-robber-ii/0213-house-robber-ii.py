class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        memo1 = {}
        memo2 = {}
        # t = n%2==0

        def f(idx, maxi_len, memo):
            # if t:
            if idx > maxi_len:
                return 0
            # else:
            #     if idx >= n-1:
            #         return 0
            if idx in memo:
                return memo[idx]

            take_i = nums[idx] + f(idx + 2, maxi_len, memo)
            skip_i = f(idx+1, maxi_len, memo)

            memo[idx] = max(take_i, skip_i)
            return memo[idx]

        return max(f(0, n-2, memo1), f(1, n-1, memo2))
        