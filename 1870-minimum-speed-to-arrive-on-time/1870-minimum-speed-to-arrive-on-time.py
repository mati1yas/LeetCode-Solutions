class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        left=1
        right=10**7
        
        ret=-1
        
        while left<=right:
            speed=(left+right)//2
            
            hours=0
            for d in dist[:-1]:
                hours+=math.ceil(d/speed)
            hours+=dist[-1]/speed
            
            if hours<=hour:
                ret=speed
                right=speed-1
            else:
                
                left=speed+1
        return ret
                
                