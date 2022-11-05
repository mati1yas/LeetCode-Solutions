class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        countBoardLetters=defaultdict(int)
        #counting letters
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                countBoardLetters[board[row][col]]+=1
        countWordLetters=Counter(word)
        
        for char in countWordLetters:
            
            if char not in countBoardLetters or countWordLetters[char]>countBoardLetters[char]:
                return False
                   
        
        
        inbound=lambda row,col: 0<=row<len(board) and 0<=col<len(board[0])
        
        def backtrack(curRow,curCol,pointer):
            if not inbound(curRow,curCol) or word[pointer]!=board[curRow][curCol] or pointer>=len(word):
                return False
            if pointer==len(word)-1:
                return True
            
            
            
            
            
            DIRS=[[1,0],[0,1],[-1,0],[0,-1]]
            temp=board[curRow][curCol]
            board[curRow][curCol]="#"
            for x,y in DIRS:
                
                if backtrack (curRow+x,curCol+y,pointer+1) :
                    return True
            board[curRow][curCol]=temp
            
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                
                if word[0]==board[row][col]:
                    if backtrack(row,col,0):
                        return True
        
        
        
        