class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        n=len(piles)
        
        memo={}
        
        
        def takeStones(start,m ,alice):
            
            if start==n:
                return 0
            
            if (start,m,alice) in memo:
                
                return memo[(start,m,alice)]
            
            pre=0
            res=float('inf') if not alice else float('-inf')
            for i in range(1,min(2*m,n-start)+1):
                
                pre+=piles[start+i-1]
                
                
                if alice:
                    
                    res= max(res,pre+takeStones(start+i,max(i,m),False))
                    
                else:
                    res= min(res,takeStones(start+i,max(i,m),True))
                
            
            
            memo[(start,m,alice)]=res
            return res
            
        
        
        
        
        return takeStones(0,1,True)