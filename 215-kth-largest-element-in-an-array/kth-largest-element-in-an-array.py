import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse = True)
        # for i in range(k+1):
        #     return nums[k-1]

        nums = [-ele for ele in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)


        


