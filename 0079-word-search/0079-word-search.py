class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        countBoardLetters=defaultdict(int)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                countBoardLetters[board[i][j]]+=1
        
        countWordLetters=Counter(word)
        
        for char in countWordLetters:
            if char not in countBoardLetters or countBoardLetters[char]<countWordLetters[char]:
                return False
        inbound=lambda row,col: 0<=row<len(board) and 0<=col<len(board[0])
        DIRS=[[1,0],[-1,0],[0,1],[0,-1]]
        def backTrack(row,col,pointer):
            
            if not inbound(row,col) or board[row][col]!=word[pointer] or pointer>=len(word):
                return False
            
            if pointer==len(word)-1:
                return True
            
            
            
            temp=board[row][col]
            board[row][col]="@"
            for x,y in DIRS:
                if backTrack(row+x,col+y,pointer+1):
                    return True
            board[row][col]=temp
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if backTrack(i,j,0):
                        return True
                