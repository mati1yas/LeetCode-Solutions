class Solution:
    def knightDialer(self, n: int) -> int:
        
        length= n
        
        n= 4
        m= 3 
        
        mod=pow(10,9)+7
        def inbound(row,col):
            
            if (row,col)==(3,2) or (row,col)== (3,0):
                return False
            
            return 0<=row<n and 0<=col<m
        
        self.memo={}
        
        DIRS= [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]
        def dial(row,col,l):
            
            if l==0:
                return 1
            if (row,col,l) in self.memo:
                return self.memo[(row,col,l)]
            r=0
            for x,y in DIRS:
                nx,ny=row+x ,col+y 
                
                
                if inbound(nx,ny) :
                    r+=dial(nx,ny,l-1)
                    
            self.memo[(row,col,l)]=r%mod
            return r%mod
        
        
        ans=0 
        
        for i in range(n):
            for j in range(m):
                if (i,j)==(3,2) or (i,j)== (3,0):
                    continue
                    
                r=dial(i,j,length-1)
                ans+=r

                
                
        return ans%mod
                
        
            
            