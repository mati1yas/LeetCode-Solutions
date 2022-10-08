class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        
        self.combs=[]
        def comb(index,arr):
            
            if len(arr)==k:
                self.combs.append(arr)
                return
            
            for i in range(index+1,n+1):
                
                comb(i,arr+[i])                      
            
              
        
        for i  in range(1,n+1):
            
            comb(i,[i])
        return self.combs
    