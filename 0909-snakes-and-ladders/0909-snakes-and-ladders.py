class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
        
        queue= collections.deque()
        
        n= len(board)
        
        gridNumber={}
        
        columns = list(range(0,n))
        
        
        number=1
        queue.append((1,0))
        ans=float('inf')
        visited=set()
        
        
        
        
        for row in range(n-1,-1,-1):
            
            for column in columns:
                
                gridNumber[number]=(row,column)
                
                number+=1
                
            columns.reverse()

    
        
        while queue:
            
            
            gridVal , count=queue.popleft()
            
            if gridVal==n*n:
                
                ans=min(ans,count)
                continue
            
            
            for next_cell in  range(gridVal + 1, min(gridVal + 6, n**2)+1):
                
                nextRow,nextCol=gridNumber[next_cell]
                
                if board[nextRow][nextCol]==-1:
                    
                    if next_cell not in visited:
                    
                        queue.append((next_cell,count+1))
                        visited.add(next_cell)
                else:
                    # next_next_row is generated from the current value
                    if board[nextRow][nextCol] not in visited:
                        visited.add(board[nextRow][nextCol])
                        queue.append((board[nextRow][nextCol],count+1))
                    
        return ans if ans!=float('inf') else -1
                    
                    
            
            