class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        
        
        
        
        
        queue=collections.deque()
        
        sea=0
        visited=set()
        land=0
        
        
        # about to start bfs from the land
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j]==1:
                    land+=1
                    queue.append((i,j,0))
                    visited.add((i,j))
                    
        
                    
                    
        
        
        DIRS=[[1,0],[0,-1],[-1,0],[0,1]]
        inbound= lambda row,col: 0<=row<len(grid) and 0<=col <len(grid[0])
        level=0
        
        while queue:
            
            
            
            curR,curC,d=queue.popleft()
            level=max(level,d)

            for x,y in DIRS:
                nx,ny=x+curR,curC+y


                if inbound(nx,ny ) and (nx,ny ) not in visited:
                    sea+=1
                    queue.append((nx,ny,d+1))
                    visited.add((nx,ny))
                        
            
            
        if not sea or not land:
            return -1
        return level
            
                
                