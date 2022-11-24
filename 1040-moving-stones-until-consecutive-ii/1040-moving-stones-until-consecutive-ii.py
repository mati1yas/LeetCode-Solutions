class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        
        arr=sorted(stones)
        
        right=0
        left=0
        n=len(arr)
        
        high=max(arr[n-1]-arr[1]-n+2,arr[n-2]-arr[0]-n+2)
        
        
        low=len(arr)
        
        
        for right in range(n):
            
            while arr[right]-arr[left]>=n:
                left+=1
            
            
            if  right-left+1==n-1 and arr[right]-arr[left]==n-2 :
                low=min(low,2)
            else:
                low=min(low,n-(right-left+1))
        
        
        return [low,high]
                
        