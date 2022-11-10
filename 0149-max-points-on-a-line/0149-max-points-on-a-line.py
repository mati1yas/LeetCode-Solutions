class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        
        
        line=0
        bigCount=0
        for x1, y1 in points:
            
            slope=defaultdict(int)
            count=0
            for x2, y2 in points:
                if x2==x1  :
                    count+=1
                    continue
                m=(y2-y1)/(x2-x1)
                slope[m]+=1
            if slope:
                line=max(line,max(slope.values()))
            bigCount=max(bigCount,count)
          
        
        return max(line+1,bigCount)