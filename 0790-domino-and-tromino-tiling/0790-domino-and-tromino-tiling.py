class Solution:
    def numTilings(self, n: int) -> int:
        
        
        mod=pow(10,9)+7
        
        
        memo_partial={}
        memo_full={}
        def partial_coverage(n):
            
            if n==2:
                return 1
            
            if n in memo_partial:
                
                return memo_partial[n]
            
            tot=full_coverage(n-2) + partial_coverage(n-1)
            memo_partial[n]=tot%mod
            return memo_partial[n]
            
        
        def full_coverage(n):
            
            
            
            if n<=2:
                return n
            
            if n in memo_full:
               
                return memo_full[n]
            
            
            tot=full_coverage(n-1)+full_coverage(n-2)+2*partial_coverage(n-1)
            memo_full[n]=tot%mod
            return memo_full[n]
        
        return full_coverage(n)