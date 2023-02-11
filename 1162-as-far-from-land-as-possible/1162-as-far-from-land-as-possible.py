class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        
        
        
        
        
        
            
        queue=collections.deque()
        visited=set()
        land=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                
                if grid[i][j]==1:
                    land+=1  # count number of land cells
                    visited.add((i,j))
                    queue.append((i,j))
        DIRS=[[1,0],[0,1],[-1,0],[0,-1]]
        

        inbound = lambda row,col : 0<=row<len(grid) and 0<=col<len(grid[0])


        distance=-1
        sea=0
        while queue:

            


            for _ in range(len(queue)):
                curRow,curCol=queue.popleft()

                for x,y in DIRS:
                    nx,ny=curRow+x,curCol+y

                    if inbound(nx,ny ) and (nx,ny) not in visited:
                        sea+=1  #  count number sea cells
                        visited.add((nx,ny))
                        queue.append((nx,ny))

            distance+=1
        if sea<1 or land<1:
            return -1
        return distance

        
        
        
            
            
        
                