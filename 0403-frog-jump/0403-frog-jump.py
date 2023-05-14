class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        
        lastStone=max(stones)
        
        stones=set(stones)
        
        self.memo={}
        
        if 1 not in stones:
            return False
        
        visited=set()
        
        def jump(k,current):
            
           
            if (k,current) in self.memo:
                
                return self.memo[(k,current)]
            
            if current not in stones:
                return False
            
            if current>lastStone:
                return False
            
            if current == lastStone:
                return True
            
            res=False
            for step in [1,0,-1]:
                
                newK= k+step
                
                if newK>0:
                    
                    res|= jump(newK,current+newK)
                        
                 
            self.memo[(k,current)]= res
            
            return res
        
        return jump(1,1)
            
            
            
            
            
            
            
            
            