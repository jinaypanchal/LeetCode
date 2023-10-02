class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        gain  = []
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                gain.append(prices[i] - prices[i-1])\
        
        return sum(gain)
        