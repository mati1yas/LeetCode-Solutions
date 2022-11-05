class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        
        
        count=0
        for divisor in range(1,min(a,b)+1):
            
            if a%divisor==0 and b%divisor==0:
                count+=1
        return count