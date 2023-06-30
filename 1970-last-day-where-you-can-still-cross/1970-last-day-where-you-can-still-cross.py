class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        
        def inbound(r,c):
            
            return 0<=r<row and 0<=c<col
        def canCross(day):
            grid = [[0] * col for _ in range(row)]
            queue= collections.deque()
            
            
            for r,c in cells[:day]:
                grid[r-1][c-1]=1
                
            
            for i in range(col):
                if not grid[0][i]:
                    queue.append((0,i))
                    grid[0][i]=-1
            
            
            while queue:               
                
                r,c = queue.popleft()
                
                if r == row-1:
                    return True
                
                
                for x,y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx,ny=r+x,c+y
                    
                    if inbound(nx,ny) and grid[nx][ny] == 0:
                        
                        grid[nx][ny] = -1
                        queue.append((nx,ny))
                
            
            
            return False
            
            
            
            
        
        left=1
        right=row*col
        
        while left<=right:
            
            mid= (left+right)//2
            
            if canCross(mid):
                
                left=mid+1
            else:
                right=mid-1
                
        return left-1