class Solution:
    @cache
    def f(self, n):
        # memo = {}
        if n == 1:
            return 1
        
        res = float('-inf')
        for i in range(1, n):
            prod = i * max(n-i, self.f(n-i))
            res = max(res, prod)
        
        return res
        
    def integerBreak(self, n: int) -> int: 
        return self.f(n)

        