class Solution:
    def addDigits(self, num: int) -> int:
        
        
        digit=num
        while True:
            
            
            tot=0
            while digit:
                last=digit%10
                digit=digit//10
                tot+=last
            
            if tot<10:
                return tot
            digit=tot