class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        
        clips.sort(key = lambda x: x[1])
        lastPos=clips[-1][1]
        clips.sort()
        dp= [float('inf') for _ in range(max(lastPos,time)+2)]
        
        
        dp[0]=0
        
        for start, end in clips:
            
            for cur in range(start+1,end+1):
                
                dp[cur]=min(dp[start]+1,dp[cur]) 
                
        
        
        return dp[time] if dp[time]!= float('inf') else -1