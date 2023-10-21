class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # n = len(nums)
        # memo = {}

        # def f(prev, curr):
        #     res = 0
        #     if curr >= n:
        #         return 0
                        
        #     if (prev, curr) in memo:
        #         return memo[(prev,curr)]
            
        #     if prev == -1 or curr - prev <= k:
        #         take = nums[curr] + f(curr, curr + 1)
        #         not_take = f(prev, curr + 1)
        #         res = max(take, not_take)
            
        #     # if res > 0:
        #     return res
        #     # else:
        #     #     return max(nums)

        # val = f(-1, 0)
        # if val > 0:
        #     return val
        # else:
        #     return max(nums)
        n = len(nums)
        t = list(nums)
        pq = []
        heapq.heappush(pq, (-t[0], 0))
        maxR = t[0]
        for i in range(1, n):
            while pq and pq[0][1] < i - k:
                heapq.heappop(pq)
            t[i] = max(t[i], nums[i] - pq[0][0])
            heapq.heappush(pq, (-t[i], i))
            maxR = max(maxR, t[i])
        
        return maxR
        