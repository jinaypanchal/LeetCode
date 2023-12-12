class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums.sort()
        # print(nums)
        # return (nums[-1]-1) * (nums[-2] -1)
        maxi = float('-inf')
        curMax = nums[0]
        for i in range(1,len(nums)):
            maxi = max(maxi, ((nums[i]-1) * (curMax-1)))
            curMax = max(curMax, nums[i])
        
        return maxi

        