class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
#         rows= set()
#         cols=set()
        
        
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
                
#                 if matrix[i][j]==0:
                    
#                     rows.add(i)
#                     cols.add(j)
                    
    
        
        
#         for i in range(len(matrix)):
#             for j in range(len(matrix[0])):
#                 if i in rows or j in cols:
#                     matrix[i][j]=0


        first_col=False
    
        for i in range(len(matrix)):
            
            
            if matrix[i][0]==0:
                first_col=True
            for j in range(1,len(matrix[0])):
                
                
                if matrix[i][j]==0:
                    
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                
                
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j]=0
                    
        
        
        if matrix[0][0]==0:
            for j in range(len(matrix[0])):
                
                matrix[0][j]=0
                
        
        if first_col:
            for i in range(len(matrix)):
                
                matrix[i][0]=0
            
        
        
        
        
        
                



    
        
        
        
        