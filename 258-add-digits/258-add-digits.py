class Solution:
    def addDigits(self, num: int) -> int:
        
        
        while len(str(num))>1:
            tot=0
            for l in str(num):
                tot+=int(l)
            num=tot
                
        return num