class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        def subBox(row,col):
            
            # checks if there is duplicate in subBox
            visited=set()
            
            count=0
            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j].isdigit():
                        # print(board[row+i][col+j])
                        visited.add(board[row+i][col+j])
                        count+=1
            
            return count==len(visited)
            
            
        
        for i in range(len(board)):
            visited=set()
            count=0
            
            # checks row wise if there is duplicate
            for j in range(len(board)):
                if board[i][j].isdigit():
                    visited.add(board[i][j])
                    count+=1
            if len(visited)!=count:
                
                return False
            visited=set()
            count=0
            # below block checks column wise
            for k in range(len(board)):
                
                if board[k][i].isdigit():
                    visited.add(board[k][i])
                    count+=1
                if i%3==0 and k%3==0:
                    if not subBox(k,i):
                        
                        return 
            if len(visited)!=count:
                
                return False
        
        return True
                    
                    