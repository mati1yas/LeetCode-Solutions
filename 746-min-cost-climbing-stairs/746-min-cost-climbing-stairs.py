class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        self.minCost=float('inf')
        memo={}
        def dfs(i):
            
            if i>=len(cost):
                
                return 0
            
            m=float('inf')
            for x in [1,2]:
                ni=i+x
                if ni not in memo:
                    m=min(m,dfs(ni))
                else:
                    m=min(m,memo[ni])
            
            memo[i]=m+cost[i]
            return memo[i]
                
            
        
        return min(dfs(0),dfs(1))
                
                
                
                