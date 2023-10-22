class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        i = k
        j = k
        n = len(nums)
        curr_min = nums[k]
        res = nums[k]

        while i > 0 or j < n - 1:
            l_val = nums[i-1] if i > 0 else 0
            r_val = nums[j+1] if j < n - 1 else 0

            if l_val > r_val:
                i -= 1
                curr_min = min(curr_min, nums[i])
            else:
                j += 1
                curr_min = min(curr_min, nums[j])
            
            res = max(res, curr_min * (j - i + 1))
        
        return res

