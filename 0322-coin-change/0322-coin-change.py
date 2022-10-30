class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo={}
        memo[0]=0
        
        if amount==0:
            return 0
    
        def dfs(current):
            
            
            minAmount=float('inf')
            for coin in coins:               
                
                if current-coin in memo:
                    minAmount=min(minAmount,memo[current-coin])
                elif current-coin>0:
                    minAmount=min(minAmount,dfs(current-coin))
            memo[current]=minAmount+1
            
            return memo[current]
        r=dfs(amount) 
        return r if r != float('inf') else -1
                    
                
                
                