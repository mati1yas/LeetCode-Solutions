class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        row=len(matrix)
        col=len(matrix[0])
        
        dp=[[0]*(col+1) for i in range(row+1)]
        
        maxLenSquare=0
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='1':
                    dp[i+1][j+1]=min(dp[i][j+1],dp[i][j],dp[i+1][j])+1
                    maxLenSquare=max(maxLenSquare,dp[i+1][j+1])
            
        
        return maxLenSquare*maxLenSquare