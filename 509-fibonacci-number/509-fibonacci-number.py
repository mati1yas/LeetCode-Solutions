class Solution:
    def fib(self, n: int) -> int:
        
        p1=0
        p2=1
        
        if n==0 or n==1:
            return n
        
       
        count=2
        while n>1:
            
            temp=p1+p2
            if count==n:
                return temp
            p1=p2
            p2=temp
            count+=1
        # return temp
            
            
            
            
            
            
            
            
       