class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
        return count
        # for i in range(len(nums)):
        #     if nums[i] not in d:
        #         d[nums[i]] = i
        #     elif d[nums[i]] in d:
        #         count += 1

        