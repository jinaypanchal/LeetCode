from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return num
                # d[num] += 1

        
        # i = 0 
        # j = i+1
        # while (j<len(nums)):
        #     if nums[i] == nums[j]:
        #         return nums[j]
        #     else:
        #         j+=1
        # count = Counter(nums)
        # for i in count.keys():
        #     if count[i] > 1:
        #         return i
