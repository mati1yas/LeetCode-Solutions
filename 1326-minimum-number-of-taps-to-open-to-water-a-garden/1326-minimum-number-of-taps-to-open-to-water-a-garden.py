class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        
        
        
        
        
        dp =  [float('inf') for i in range(n+1)]
        
        
        dp[0]=0
        
        
        for cur in range(n+1):
            
            cover_start= max(0,cur-ranges[cur])
            
            cover_end= min(n,cur+ranges[cur])
            
            for prev in range(cover_start,cover_end+1):
                
                dp[cover_end]=min(dp[cover_end],dp[prev]+1)
                
    
        
        return dp[n] if dp[n]!= float('inf') else -1
        
        