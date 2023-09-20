class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        low = 1
        high = max(quantities)
        def check(t):
            li = [math.ceil(num / t) for num in quantities]
            return sum(li) > n

        while low <= high:
            mid = (low + high)//2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1
        
        return low
        