class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        
        
        Area1=(ax2-ax1)*(ay2-ay1)
        Area2=(bx2-bx1)*(by2-by1)
        
        
        intersectWidth=max(0,min(ax2,bx2)-max(ax1,bx1))    # elieminates if width is negative 
        intersectLength=max(0,min(ay2,by2)-max(by1,ay1))       # eliminates if  length is negative 
        intersectArea=intersectWidth*intersectLength
        
        print(intersectArea)
        
        return Area1+Area2- intersectArea
        
        
        