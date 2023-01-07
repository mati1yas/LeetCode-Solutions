class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        count=0
        
        for row in grid:
            
            for i  in range(len(grid)):
                column=[]
                for j in range(len(grid)):
                    column.append(grid[j][i])
                
                if column==row:
                    count+=1
        return count
                    