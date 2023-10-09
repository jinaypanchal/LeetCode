class Solution:
    def climbStairs(self, n: int) -> int:
        memo ={}
        def  f(n):
            if n < 0:
                return 0
            
            if n == 0:
                return 1
            
            if n in memo:
                return memo[n]
            
            memo[n] = f(n-1) + f(n-2)
            
            # t = 0
            # t += f(n-1)
            # t += f(n-2)
            return memo[n]

        
        return f(n)
        