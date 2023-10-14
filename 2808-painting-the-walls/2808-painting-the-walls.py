class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        memo = {}
        n = len(time)
        def f(idx, rem_walls):
            if rem_walls <= 0:
                return 0
            
            if idx >= n:
                return 1e9
            
            if (idx, rem_walls) in memo:
                return memo[(idx, rem_walls)]
            
            paint = cost[idx] + f(idx + 1, rem_walls - time[idx] - 1)
            notpaint = f(idx + 1, rem_walls)

            memo[(idx, rem_walls)] = min(paint, notpaint)

            return memo[(idx, rem_walls)]
        

        return f(0, n)
        