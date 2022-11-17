class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        xOverLap=max(0,min(rec1[2],rec2[2])-max(rec1[0],rec2[0]))
        yOverLap=max(0,min(rec1[3],rec2[3])-max(rec1[1],rec2[1]))
        intersectArea=xOverLap*yOverLap
        
        return intersectArea!=0