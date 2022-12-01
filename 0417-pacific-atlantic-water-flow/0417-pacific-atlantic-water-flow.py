class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific, atlantic = set(), set()
        
        row, col = len(heights),len(heights[0])
        
        DIRS= [[1,0],[0,1],[-1,0],[0,-1]]
        visited=set()
        def dfs(r,c,prevHeight,ocean):
            
            if  (r<0 or c<0 or r==row or c==col )or prevHeight>heights[r][c] or (r,c) in ocean :
                return 
            
            
            ocean.add((r,c))
            for x , y in DIRS:
                newr,newc= r+x,c+y
                
                dfs(newr,newc,heights[r][c],ocean)
                
            
            
            
        
        for c in range(col):
            dfs(0,c,heights[0][c],pacific)
            dfs(row-1,c,heights[row-1][c],atlantic)
            
            
        for r in range(row):
            dfs(r,0,heights[r][0],pacific)
            dfs(r,col-1,heights[r][col-1],atlantic)
            
        res=[]
        for r in range(row):
            for c in range(col):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
        
            
        
        