class Solution:
    def minOperations(self, nums: List[int]) -> int:        

        t = sorted((set(nums)))
        n = len(nums)
        res = n
        j = 0
        for i in range(len(t)):
            l = t[i]
            r = l + n - 1
            # j = i
            while j < len(t) and t[j] <= r:
                j += 1
            
            in_range = j-i
            out_range = n - in_range
               
            res = min(res, out_range)
        
        return res


        