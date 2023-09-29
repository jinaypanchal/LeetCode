class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(1, len(nums)):
            if nums[i] >  nums[i-1]:
                dec = False
            elif nums[i] < nums[i-1]:
                inc = False
            
            if not inc and not dec:
                return False
        return True
        # def increasing(nums):
        #     inc = True
        #     for i in range(1, len(nums)):
        #         if nums[i] < nums[i-1]:
        #             inc = False
        #     return inc
        
        # def decreasing(nums):
        #     dec = True
        #     for i in range(1, len(nums)):
        #         if nums[i] > nums[i-1]:
        #             dec = False
        #     return dec
        
        # return increasing(nums) or decreasing(nums)

        
        