class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        
        
        visited=set()
        
        DIRS=[[1,0],[0,1],[-1,0],[0,-1]]
        
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        self.atEdge=False
        
        def dfs(row,col):
            
            
            
            for x,y in DIRS:
                nx,ny = row+x,col+y    
                
                if not inbound(nx,ny) :
                    self.atEdge=True
                
                if inbound(nx,ny) and grid[nx][ny] and (nx,ny) not in visited:
                    self.connected+=1
                    
                    visited.add((nx,ny))
                    dfs(nx,ny)
                
        
        
        self.totalOnes=0
        self.connected=0
        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]:
                    self.totalOnes+=1
                    
                self.atEdge=False 
                if grid[i][j] and (i,j) not in visited: 
                    
                    self.connected+=1
                    visited.add((i,j))
                    dfs(i,j)
                    
                    if self.atEdge:
                        self.totalOnes-=self.connected
                    self.connected=0
                    
                    
        return self.totalOnes
                    
                
                    
                    