class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        
        DIRS = ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2))
        
        
        
        
        
        def inbound(row,col):
            
            return 0<= row<n and 0<=col<n
        
        memo={}
        
        def moveKnight(row,col,moves):
            
            if moves==0:
                return 1
            if (row,col,moves) in memo:
                return memo[(row,col,moves)]
            
            tot=0
            for x,y in DIRS:
                
                nr,nc=row+x,col+y
                
                if inbound(nr,nc) :
                    tot += moveKnight(nr,nc,moves-1)
            memo[(row,col,moves)]=tot
            return tot
        
        return moveKnight(row,column,k)/8**k
            