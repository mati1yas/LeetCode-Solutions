class Solution:
    def findComplement(self, num: int) -> int:
        n = len(bin(num)[2:]) - 1
        
        ans=0
        for i in range(n,-1,-1):
            
            
            bit = 0 if num & (1 << i )  else 1
            
            ans= (ans<<1)|bit
            
            
        return ans