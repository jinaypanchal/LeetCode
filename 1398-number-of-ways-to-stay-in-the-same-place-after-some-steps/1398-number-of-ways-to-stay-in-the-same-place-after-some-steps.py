class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        memo = {}
        mod = 10**9 + 7
        def f(idx, n):
            if idx - 0 > n:
                return 0
            
            if idx >= arrLen or idx < 0:
                return 0 
            if (idx, n) in memo:
                return memo[(idx,n)]

            if n == 0:
                if idx == 0:
                    return 1
                else:
                    return 0

            ct = 0
            ct += f(idx - 1, n-1) #left
            ct += f(idx, n-1) #stay
            ct += f(idx + 1, n-1) #right
            memo[(idx, n)] =  ct % mod

            return memo[(idx,n)]

        return f(0, steps)


        