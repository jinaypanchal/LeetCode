class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo ={}
        n = len(nums)

        def f(idx, p):
            if (idx, p) in memo:
                return memo[(idx,p)]
            
            if idx >=n :
                return p
            
            take_i = f(idx+1, p*nums[idx])
            skip_i = f(idx+1, nums[idx])

            memo[(idx, p)] = max(take_i, skip_i, p)

            return memo[(idx,p)]
        
        return f(1, nums[0])
            
