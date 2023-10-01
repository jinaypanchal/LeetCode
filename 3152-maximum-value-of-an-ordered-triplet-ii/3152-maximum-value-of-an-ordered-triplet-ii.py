class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return 0

        pref_max = [0] * n
        pref_max[0] = nums[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], nums[i])

        suff_max = [0] * n
        suff_max[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suff_max[i] = max(suff_max[i + 1], nums[i])

        ans = 0

        for j in range(1, n - 1):
            triplet_value = (pref_max[j - 1] - nums[j]) * suff_max[j + 1]
            ans = max(ans, triplet_value)

        return max(0, ans)
        