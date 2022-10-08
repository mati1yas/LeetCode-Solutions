class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        for mat in matrix:
            
            l=0
            r=len(mat)-1
            
            if mat[0]>target:
                return False
            while l<=r:
                
                mid=(l+r)//2
                
                if mat[mid]>target:
                    
                    r=mid-1
                elif mat[mid]<target:
                    l=mid+1
                else:
                    
                    return True
        
        
        