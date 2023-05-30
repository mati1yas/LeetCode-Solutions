class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
    
        memo={}
        n=len(stoneValue)
        
        
        
        def takeStone(start,alice):
            
            
            
            if start>=n:
                return 0
            
            if start in memo:
                return memo[start]
            
            res= float('inf') if not alice else float('-inf') 
            
            pre=0
            for x in range(1,min(3,n-start)+1):
                pre+=stoneValue[start+x-1]
                
                
                
                res = max(res,pre-takeStone(start+x,True))
                    
                
            memo[start]=res  
            return res
        
        ret=takeStone(0,True)
        if ret>0:
            return "Alice"
        elif ret<0:
            return "Bob"
        else:
            return "Tie"
        
                
                
                