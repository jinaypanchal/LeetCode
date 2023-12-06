class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        mon = 1
        while n > 0:
            money = mon
            for d in range(1, min(n, 7) + 1):
                res += money
                money += 1
            
            n -= 7
            mon += 1
        
        return res
        