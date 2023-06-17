class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        
        arr2.sort()
        
        
        
        
        
        memo={}
        def dfs(prev,idx1):
            
            if idx1==len(arr1):
                
                return 0
            if (prev,idx1) in memo:
                return memo[(prev,idx1)]
            
            minOperation=float('inf')
            if arr1[idx1]>prev:
                minOperation = dfs(arr1[idx1],idx1+1)
                
            nextGreaterIdx=bisect.bisect_right(arr2,prev)
            
            if nextGreaterIdx<len(arr2):
                i=nextGreaterIdx
                minOperation=min(minOperation,1+dfs(arr2[i],idx1+1))
            memo[(prev,idx1)]=minOperation
            return minOperation
        r=dfs(float('-inf'),0)
        if r!= float('inf'):
            return r
        else:
            return -1
        
            
            
            
            