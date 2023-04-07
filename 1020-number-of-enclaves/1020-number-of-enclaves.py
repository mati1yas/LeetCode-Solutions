class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        
        
        visited=set()
        
        DIRS=[[1,0],[0,1],[-1,0],[0,-1]]
        
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        self.totalOnes=0
        def dfs(row,col):
            
            for x,y in DIRS:
                nx,ny = row+x,col+y    
                
                if not inbound(nx,ny) :
                    self.atEdge=True
                
                if inbound(nx,ny) and grid[nx][ny] and (nx,ny) not in visited:
                      
                    visited.add((nx,ny))
                    dfs(nx,ny)
        

        
        for  i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.totalOnes+=1
                    
                if grid[i][j] and (i,j) not in visited and (i==0 or j==0 or i==len(grid)-1 or j==len(grid[0])-1): 
                    
                    visited.add((i,j))
                    dfs(i,j)
                    
                    
                    
        return self.totalOnes-len(visited)
                    
                
                    
                    