class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        
        DIRS=[[1,0],[0,1],[0,-1],[-1,0]]
        
        def inbound(row,col):
            
            return 0<=row<m and  0<=col<n
        
        visited = set()
        
        outLeading={}
        
        def countPaths(row,col,moves):
            
            
            if moves==0:
                return 0
            
            
            count=0
            
            if (row,col,moves) in outLeading:
                return outLeading[(row,col,moves)]
            for x,y in DIRS:
                nr,nc=row+x,col+y
                
                if inbound(nr,nc) :
                    count+=countPaths(nr,nc,moves-1)
                else:
                    count+=1
                    
                
            outLeading[(row,col,moves)]=count
                    
                    
            return count
        mod=pow(10,9)+7
        return countPaths(startRow,startColumn,maxMove)%mod
                    
            
            
            
            
            