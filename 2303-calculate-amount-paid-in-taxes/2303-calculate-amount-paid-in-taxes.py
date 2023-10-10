class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        
        
        
        totalTax=0
        
        
        
        for idx,(upper,rate) in enumerate(brackets):
            
            
            current=upper-brackets[idx-1][0] if idx>=1 else upper- 0
            
            totalTax+=(min(current,income))*(rate/100)
            income=income-current
            if income<=0:
                break
        
        return totalTax