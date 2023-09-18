class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums) + 1

        def checker(mid):
            res = 0
            for n in nums:
                res += math.ceil(n/mid)
            
            return res <= threshold


        while low <= high:
            mid = (low+high)//2
            if checker(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low



        for i in range(1,1000001):
            sumi = 0
            for num in nums:
                sumi += math.ceil(num/i)
            if sumi <= threshold:
                break
        
        return i
        





        