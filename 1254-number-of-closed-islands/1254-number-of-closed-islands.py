class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        
        
        visited=set()
        
        leftBoundary=topBoundary=0
        rightBoundary=len(grid[0])-1
        bottomBoundary=len(grid)-1
        
        def inbound(row,col):
            return  0<=row<len(grid) and 0<=col<len(grid[0])
        
       
        DIRS=[[0,1],[1,0],[-1,0],[0,-1]]
        
        
        self.onBorder=False
        
        def dfs(row,col):
            
            nonlocal leftBoundary,topBoundary,rightBoundary,bottomBoundary
            
            if col==leftBoundary or row==bottomBoundary or col==rightBoundary or row==topBoundary:
                self.onBorder=True
            
            for x,y in DIRS:
                
                nx,ny=row+x,col+y
                
                if inbound(nx,ny) and (nx,ny) not in visited and grid[nx][ny]==0:
                    
                    
                    
                    visited.add((nx,ny))
                    dfs(nx,ny)
            
            
        self.count=0    
             
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]==0 and (i,j) not in visited:
                    
                    visited.add((i,j))
                    dfs(i,j)

                    if not self.onBorder:
                        self.count+=1
                        
                    self.onBorder=False
                        
        return self.count
                        
                
                    # lTmost=(i,j)
                    
        