class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        
        
        
        DIRS=[[-1,0],[0,-1],[1,0],[0,1]]
        
        dp=[[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        
        def inbound(row,col):
            
            return 0<=row<len(mat) and 0<=col<len(mat[0])
        
        
        queue=deque()


        visited=set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]==0:
                    queue.append((i,j,0))
                    visited.add((i,j))
                    
                    
                    

        while queue:

            curx,cury,dist=queue.popleft()

            

            for x,y in DIRS:

                nr,nc= curx+x,cury+y

                if inbound(nr,nc) and (nr,nc) not in visited:

                    queue.append((nr,nc,dist+1))            
                    visited.add((nr,nc))
                    dp[nr][nc]=dist+1
            
        
        
                
        return dp
            
            