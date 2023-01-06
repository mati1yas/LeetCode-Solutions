class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:



        start=None
        end=None
        points.sort()
        count=0
        for p1,p2 in points:

            if not start and not end:
                start=p1
                end=p2
            else:

                if p1<=end:                   
                    end=min(end,p2)
                else:
                    
                    count+=1
                    start=p1
                    end=p2
        
        
     
        return count+1

