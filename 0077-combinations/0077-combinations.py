class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        self.ans=[]
        def combine(index,k,combs):
            
            
            if k==0:
                
                self.ans.append(combs)
                
    
                return 
    
    
            
            for val in range(index,n+1):
                combine(val+1,k-1,combs+[val])
                
                
            
        combine(1,k,[])
        return self.ans
                