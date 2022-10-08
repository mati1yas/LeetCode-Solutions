class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l=0
        r=len(matrix)-1
        foundAt=float('inf')
        while l<=r:
            
            mid=(l+r)//2
            
            if matrix[mid][0]>target:
                r=mid-1
            else:
                l=mid+1
                foundAt=mid
        
      
        
        if foundAt==float('inf'):
            return False
        
        arr=matrix[foundAt]
        
        left=0
        right=len(arr)-1
       
        while left<=right:
            
            mid=(left+right)//2
            
            if arr[mid]>target:
                right=mid-1
            elif arr[mid]<target:
                left=mid+1
            else:
                
                return True
        return False