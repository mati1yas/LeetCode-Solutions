class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        
        total=0
        count=0
        while numBottles:
            
            total+=1
            count+=1
            numBottles-=1
            if count==numExchange:
                count=0
                numBottles+=1
                
        return total