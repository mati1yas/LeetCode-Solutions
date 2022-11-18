class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        DIRS=[[0,1],[1,0],[-1,0],[0,-1],[-1,1],[1,1],[1,-1],[-1,-1]]
        
        newBoard=[[0]*(len(board[0])) for i in range(len(board))]
        
        inbound=lambda row,col : 0<=row<len(board) and 0<=col<len(board[0])
        
        
        
        def countLives(row,col):
            count=0
            
            for x,y in DIRS:
                
                if inbound(row+x,y+col) and board[row+x][col+y]==1:
                    count+=1
            
            
            return count
                    
            
            
            
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                livingNeighbours=countLives(i,j)
                
                if board[i][j]==1:
                    if livingNeighbours<2 or livingNeighbours>3:
                        newBoard[i][j]=0
                    else:
                        newBoard[i][j]=1
                        
                else:
                    if livingNeighbours==3:
                        newBoard[i][j]=1
                        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j]=newBoard[i][j]
        
        
                        
            
        
        
        
        
        