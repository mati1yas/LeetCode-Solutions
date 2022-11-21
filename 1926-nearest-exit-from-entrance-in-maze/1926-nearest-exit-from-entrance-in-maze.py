class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        
        DIRS=[[1,0],[-1,0],[0,1],[0,-1]]
        
        queue=collections.deque()
        start=(entrance[0],entrance[1])
        
        visited=set({start})
        queue.append(start)
        
        
        inbound=lambda row,col: 0<=row<len(maze) and 0<=col<len(maze[0])
        
        steps=0
        while queue:
            
            
            for i in range(len(queue)):
                
                curx,cury=queue.popleft()
                
                
                for x,y in DIRS:
                    newx,newy=curx+x,cury+y
                    if start!=(curx,cury) and not inbound(newx,newy):
                        
                        return steps
                
                for x,y in DIRS:
                    newx,newy=curx+x,cury+y
                    if (newx,newy) not in visited and inbound(newx,newy) and maze[newx][newy]=='.':
                        visited.add((newx,newy))
                        queue.append((newx,newy))
            steps+=1
        
        return -1