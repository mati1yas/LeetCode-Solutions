class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        revers=0
        n=x
        while n>0:
            r=n%10
            n//=10
            
            revers=revers*10+r
        return revers == x           
        