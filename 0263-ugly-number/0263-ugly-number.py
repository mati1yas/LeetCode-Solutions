class Solution:
    def isUgly(self, n: int) -> bool:
        
        
        if n==0:
            return False
        
        def factorize(num,prime):
            
            while num%prime==0:
                num/=prime
            
            return num
            
            
            
            
            
        for prime in [2,3,5]:
            
            n=factorize(n,prime)
        
        return n==1
        