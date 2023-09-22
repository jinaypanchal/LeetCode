class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        d = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        ct = 0
        for num in d:
            if k == 0:
                if d[num] > 1:
                    ct += 1
            elif k + num in d:
                ct += 1

        return ct
         
        
            



        