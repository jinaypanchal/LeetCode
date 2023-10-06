class Solution:
    def __init__(self):
        self.memo = {}
    # @cache
    def f(self, n):
        if n == 1:
            return 1
        
        if n in self.memo:
            return self.memo[n]
        
        res = float('-inf')
        for i in range(1, n):
            prod = i * max(n-i, self.f(n-i))
            res = max(res, prod)
        
        self.memo[n] = res
        return self.memo[n]
        
    def integerBreak(self, n: int) -> int: 
        return self.f(n)

        