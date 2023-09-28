class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []

        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        
        return even + odd
        # i = 0 
        # j = len(nums) - 1

        # while i < j:
        #     while i < len(nums) and nums[i] %2 == 0:
        #         i += 1
            
        #     while j >= 0 and nums[j]%2 == 1:
        #         j -= 1
            
        #     if  i < j:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i += 1
        #         j -= 1
        
        # return nums


