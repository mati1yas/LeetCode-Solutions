class Solution:
    def maximumSwap(self, num: int) -> int:
        
        digits=list(str(num))
        
        ans=digits[:]
        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                
                digits[i],digits[j]=digits[j],digits[i]
                
                if digits>ans:
                    ans=digits[:]
                digits[i],digits[j]=digits[j],digits[i]
                
        
        return int(''.join(ans))
                    
        
        