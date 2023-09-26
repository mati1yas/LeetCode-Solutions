class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        
        arr = [x for x in range(1,n+1)]
        start = 0  
        while True:
            
            if len(arr)==1:
                return arr[0]
            
            
            remove=(start+k-1)%len(arr)
            
            arr.pop(remove)
            
            start=remove
        