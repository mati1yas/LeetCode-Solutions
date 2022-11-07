class Solution:
    def maximum69Number (self, num: int) -> int:
        
        number=list(str(num))
        for idx,digit in enumerate(number):
            
            if digit=="6":
                number[idx]="9"
                break
        
        return int(''.join(number))