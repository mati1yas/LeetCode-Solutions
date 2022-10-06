class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        grid=[[0]*(n+1) for x in range(m+1)]
        
        # grid[m-2][n-1]=1
        # grid[m-1][n-2]=1
        grid[m-1][n-1]=1
        
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if col==n-1 and row==m-1:
                    continue
                down=grid[row+1][col]
                right=grid[row][col+1]
                grid[row][col]=down+right
                
        return grid[0][0]