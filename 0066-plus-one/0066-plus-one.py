class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.insert(0,0)
        carry=1
        pointer=len(digits)-1
        while carry!=0:
            
            if digits[pointer]+carry>9:
                carry=1
                digits[pointer]=0
                pointer-=1
            else:
                digits[pointer]+=1
                carry=0
        
        return digits if digits[0]!=0 else digits[1:]
            
            
            
        
            
            
            