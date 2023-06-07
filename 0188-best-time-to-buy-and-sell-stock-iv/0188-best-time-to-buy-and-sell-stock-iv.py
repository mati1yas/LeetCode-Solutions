class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        memo={}
        def dfs(index,state,trans):
            
            if index>=len(prices):
                return 0
            if trans==k:
                return 0
            
            if (index,state,trans) in memo:
            
                return memo[(index,state,trans)]
            profit=0
            if state:
                
                sell=prices[index]+dfs(index+1,False,trans+1)
                not_sell=dfs(index+1,True,trans)
                profit=max(sell,not_sell)
            else:
                buy=dfs(index+1,True,trans)-prices[index]
                not_buy=dfs(index+1,False,trans)
                
                profit=max(buy,not_buy)
            memo[(index,state,trans)]=profit
            return profit
        
              
        
        return dfs(0,False,0)