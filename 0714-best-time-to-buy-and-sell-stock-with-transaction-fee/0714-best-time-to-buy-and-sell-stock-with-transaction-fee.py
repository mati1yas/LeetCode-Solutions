class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo={}
        
        def dfs(idx,state):
            
            if idx>=len(prices):
                return 0
            
            
            if (idx,state) in memo:
                return memo[(idx,state)]
            
            if state:
                
                
                sell = prices[idx] + dfs(idx + 1, False) - fee
                skip = dfs(idx + 1, True)
                
                
                    
                memo[(idx, state)] = max(sell, skip)
                    
                    
                    
            else:
                buy = dfs(idx,True) - prices[idx]
                not_buy= dfs(idx+1,False)
                
                memo[(idx, state)] = max(buy,not_buy)
            
            return memo[(idx, state)]
        return dfs(0,False)