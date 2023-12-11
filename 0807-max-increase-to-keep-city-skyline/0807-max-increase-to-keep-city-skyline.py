class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        
        rowMax= defaultdict(int)
        
        colMax= defaultdict(int)
        
        
        for i in range(len(grid)):
            
            for j in range(len(grid)):
                
                rowMax[i]=max(rowMax[i],grid[i][j])
                colMax[j]=max(colMax[j],grid[i][j])
                
        total=0 
        for i in range(len(grid)):
            for j in range(len(grid)):
                
                if grid[i][j ]  in [rowMax[i],colMax[j]]:
                    continue
                   
                prev=grid[i][j]
                grid[i][j]=min(rowMax[i],colMax[j])
                total+=abs(grid[i][j]-prev)
                
   
                
        return total
                