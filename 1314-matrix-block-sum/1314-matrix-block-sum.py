class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
       
        cummulativeSum = mat[:][:]  
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                
                top=0
                left=0
                topLeft=0
                
                if i>0:
                    top=cummulativeSum[i-1][j]
                if j>0:
                    left=cummulativeSum[i][j-1]
                if i>0 and j>0:
                    topLeft=cummulativeSum[i-1][j-1] 
                    
                # BUILDS COMMULATIVE SUM FOR THE I,J CELL
                cummulativeSum[i][j] += top+left-topLeft
		
		
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                ans[i][j] = cummulativeSum[min(i+k, len(mat)-1)][min(j+k, len(mat[0])-1)] 
                ans[i][j]+=(cummulativeSum[i-k-1][j-k-1] if i-k > 0 and j-k > 0 else 0)
                ans[i][j]-= (cummulativeSum[i-k-1][min(j+k,len(mat[0])-1)] if i-k > 0 else 0)
                ans[i][j]-=  (cummulativeSum[min(i+k, len(mat)-1)][j-k-1] if j-k > 0 else 0)          
        return ans