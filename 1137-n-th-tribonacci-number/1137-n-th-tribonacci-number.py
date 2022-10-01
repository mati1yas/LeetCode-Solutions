class Solution:
    def tribonacci(self, n: int) -> int:
        
        
        self.trib={}
        def tri(n):
            
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            
            if n not in self.trib:
                self.trib[n]=tri(n-3)+tri(n-2)+tri(n-1)
            return self.trib[n]
        return tri(n)