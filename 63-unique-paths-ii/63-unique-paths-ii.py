class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dr=len(obstacleGrid)-1
        dc=len(obstacleGrid[0])-1
        if obstacleGrid[dr][dc]==1 or obstacleGrid[0][0]:
            return 0
        obstacleGrid[dr][dc]=1
        obstacleGrid.append([0]*(dc+1))
        
        for row in obstacleGrid:
            row.append(0)
            
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                if row==dr and dc==col:
                    continue
                down=0
                right=0
                if obstacleGrid[row][col]==0:
                    if obstacleGrid[row+1][col]!="X":
                        down=obstacleGrid[row+1][col]
                    if obstacleGrid[row][col+1]!="X":
                        right=obstacleGrid[row][col+1]
                    obstacleGrid[row][col]=down+right
                else:
                    obstacleGrid[row][col]="X"
        return obstacleGrid[0][0]
        
        