class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        DIRS=[[1,0],[0,1],[-1,0],[0,-1],[-1,1],[1,-1],[1,1],[-1,-1]]
        
        queue=collections.deque()
        
        n=len(grid)
        m=len(grid[0])
        
        if grid[0][0]==1 or grid[n-1][m-1]:
            return -1
        queue.append((0,0,1))  # row,col,dis
        
        
        
        inbound=lambda row,col : 0 <=row<n and 0<=col < m
        
        minDist=float("inf")
        visited=set()
        while queue:
            
            curRow,curCol,dis=queue.popleft()
            
            if curRow==n-1 and curCol==m-1:
                minDist=min(minDist,dis)
            
            for x,y in DIRS:
                nx,ny=curRow+x,curCol+y
                
                
                if inbound(nx,ny ) and grid[nx][ny]==0 and (nx,ny) not in visited:
                    
                    visited.add((nx,ny))
                    queue.append((nx,ny,dis+1))
                    
        
        if minDist==float('inf'):
            return -1
        return minDist