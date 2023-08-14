class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        
        
        
        DIRS=[[1,0],[0,1],[-1,0],[0,-1]]
        
        
        
        
        def inbound(row,col):
            
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        
        queue=collections.deque()
        queue.append((start[0],start[1],0))
        ans=[]
        visited=set({(start[0],start[1])})
        while queue:
            
            curx,cury,dist=queue.popleft()
            
            if  pricing[0]<=grid[curx][cury]<=pricing[1]:
                ans.append((dist,grid[curx][cury],curx,cury))
            
            for x,y in DIRS :
                
                nr,nc = curx+x,cury+y
                
                if inbound(nr,nc) and grid[nr][nc]!=0 and (nr,nc) not in visited :
                    
                    queue.append((nr,nc,dist+1))
                    visited.add((nr,nc))
                    
                    
                        
                        
            
        ans.sort()
        
        ret=[]
        for i in range(min(k,len(ans))):
            
            ret.append([ans[i][2],ans[i][3]])
            
        return ret