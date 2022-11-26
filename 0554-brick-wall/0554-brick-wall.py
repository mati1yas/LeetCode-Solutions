class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        ends=defaultdict(int)
        for row in wall:
            
            pre=0
            ends[pre]+=1
            for brick in row:
                pre+=brick
                ends[pre]+=1
        
        
        crossed=float('inf')
        rows=len(wall)
        
        
        for key in ends:
            
            if key==min(ends) or key==max(ends):
                
                continue
            crossed=min(crossed,rows-ends[key])
        
        return crossed if crossed!=float('inf') else rows
            
            
            
                