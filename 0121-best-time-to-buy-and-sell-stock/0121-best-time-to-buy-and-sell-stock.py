class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        maxProfit=0
        dp=[(0,0)]
        for price in prices[::-1]:
            better=max(dp[-1])
            maxProfit=max(maxProfit,better-price)
            dp.append((price,better))
        return maxProfit
            
            