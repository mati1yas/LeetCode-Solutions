class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left=1
        
        right=max(time)*totalTrips
        
        
        
        def canComplete(mid):
            trips=0
            
            for t in time:
                trips+=mid//t
                
            
            return trips>=totalTrips
        
        ans=float('inf')
        while left<=right:
            mid=(left+right)//2
            
            
            if canComplete(mid):
                right=mid-1
                ans=min(mid,ans)
                
            else:
                left=mid+1
        
        return ans
                
            