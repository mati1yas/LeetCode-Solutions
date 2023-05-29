class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        
        
        
        
        memo = {}
        cuts=[0]+sorted(cuts)+[n]
        
        def cut(left,right):
            
            if (left,right) in memo:
                return memo[(left,right)]
            
            if left+1==right:
                return 0
            m=float('inf')
            
            
            for cutPoint in range(left+1,right):
                m=min(m,cut(left,cutPoint)+cut(cutPoint,right)+cuts[right]-cuts[left])
                
                
            memo[(left,right)]=m
            
            return m
            
        
        
        
        return cut(0,len(cuts)-1)
            
            