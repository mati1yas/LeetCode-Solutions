class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        
        
        
        (p1x,p1y), (p2x,p2y) = coordinates[0],coordinates[1]
        
        
        
        for x,y in coordinates:                         
            if (p2y-p1y)*(x-p2x) != (p2x-p1x)*(y-p2y):
                return False
            
        return True