class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        column=set()  
        posdiag=set()  # (row+col)
        
        negdiag=set()  # (row-col)
        
    
        chess=[ ['.']*n for i in range(n)]
        
        self.res=[]
        def place(row):
            
            
            if row==n:
                pos=[''.join(r) for r in chess]
                
                self.res.append(pos)
                
            for col in range(n):
                if col in column or row+col in posdiag or row-col in negdiag:
                    continue
                
                column.add(col)
                posdiag.add(row+col)
                negdiag.add(row-col)
                
                chess[row][col]="Q"
                
                place(row+1)
                column.remove(col)
                posdiag.remove(row+col)
                negdiag.remove(row-col)
                
                chess[row][col]="."
                
                
                
        place(0)
          
        return self.res
        
        
                
                
            
            
            
            
            
            
            
            
        
        