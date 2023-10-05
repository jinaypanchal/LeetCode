class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        l = len(nums)
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        for key, val in d.items():
            if val > math.floor(l/3):
                res.append(key)
        return res

        