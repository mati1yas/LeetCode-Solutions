class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        turn=0
        row=[0]*len(board)
        col=[0]*len(board)
        
        diag=0
        antiDiag=0
        oWin=False
        xWin=False
        
        for i in range(len(board)):
            for j in range(len(board)):
                
                if board[i][j]=='X':
                    row[i]+=1
                    col[j]+=1
                    
                    turn+=1
                    
                    if i==j:
                        diag+=1
                    if i+j==2:
                        antiDiag+=1
                    
                    
                elif board[i][j]=="O":
                    row[i]-=1
                    col[j]-=1
                    
                    turn-=1
                    
                    if i==j:
                        diag-=1
                    if i+j==2:
                        antiDiag-=1
                        
        xWin=row[0]==3 or row[1]==3 or row[2]==3 or col[0]==3 or col[1]==3 or col[2]==3 or diag==3 or antiDiag==3
        oWin=row[0]==-3 or row[1]==-3 or row[2]==-3 or col[0]==-3 or col[1]==-3 or col[2]==-3 or diag==-3 or antiDiag==-3
        
        
        if (xWin and turn==0) or (oWin and turn==1):
            return False
        return  (turn==1 or turn == 0 ) and ( not xWin or not oWin)
        