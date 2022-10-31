class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        
        diagonal={}
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                
                if col-row not in diagonal:
                    diagonal[col-row]=matrix[row][col]
                
                else:
                    
                    if diagonal[col-row]!=matrix[row][col]:
                        return False
        return True
                    