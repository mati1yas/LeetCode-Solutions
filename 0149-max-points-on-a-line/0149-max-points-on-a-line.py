class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        
        
        line=0
        verticalMax=0
        for x1, y1 in points:
            
            slope=defaultdict(int)
            verticalPoint=0
            for x2, y2 in points:
                if x2==x1  :
                    verticalPoint+=1
                    continue
                m=(y2-y1)/(x2-x1)
                slope[m]+=1
            if slope:
                line=max(line,max(slope.values()))
            verticalMax=max(verticalMax,verticalPoint)
          
        
        return max(line+1,verticalMax)