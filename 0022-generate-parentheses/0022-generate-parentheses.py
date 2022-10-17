class Solution:
    def __init__(self):
        self.parenthesis=[]
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        self.generate('',0,0,n)
        return self.parenthesis
    def generate(self,s,opening,closing,n):
        
        
        if opening==closing==n:
            self.parenthesis.append(s)
            return
        if opening<n:
            
        
            self.generate(s+'(',opening+1,closing,n)
        
        if closing<opening:
            self.generate(s+')',opening,closing+1,n)
            
        