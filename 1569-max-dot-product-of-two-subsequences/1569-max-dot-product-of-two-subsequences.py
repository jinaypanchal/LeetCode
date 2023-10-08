class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        #mistake you did - returning 0 from BC, but it should be non-empty,hence return -infinity
        memo = {}

        def f(idx1, idx2):
            if idx1 == len(nums1) or idx2 == len(nums2):
                return float('-inf')
            
            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            val = nums1[idx1] * nums2[idx2]

            taking_idx1_idx2 = val + f(idx1+1, idx2+1)

            taking_idx1 = f(idx1+1, idx2)

            taking_idx2 = f(idx1, idx2+1)

            memo[(idx1, idx2)] = max(val, taking_idx1_idx2, taking_idx1, taking_idx2)

            return memo[(idx1, idx2)]

        return f(0, 0)
        