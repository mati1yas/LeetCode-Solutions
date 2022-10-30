class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        large=0
        
        for i in range(len(number)): 
            
            if number[i]==digit:
                large=max(large, int(number[0:i]+number[i+1:]))
                
        return str(large)