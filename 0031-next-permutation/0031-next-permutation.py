class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return 

        check = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                check = i
                break
        
        if check == -1:
            nums.reverse()
            return 

        for i in range(n-1, check, -1):
            if nums[i] > nums[check]:
                nums[check], nums[i] = nums[i], nums[check]
                break
        
        nums[check + 1 :] = nums[check + 1 :][::-1]

        