class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n=len(mat)
        m=len(mat[0])
        row=0
        col=0
        total=0
        visited=set()
        while row<n and col<m:
            total+=mat[row][col]
            visited.add((row,col))
            
            row+=1
            col+=1
        
        
        row=n-1
        col=0
        while row>=0 and col<m:
            
            if (row,col) not in visited:
                total+=mat[row][col]
            
            
            row-=1
            col+=1
        
        return total
        