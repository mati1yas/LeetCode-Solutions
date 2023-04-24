import heapq as h
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        
        arr=[-x for x in stones]
        
        h.heapify(arr)
        
        
        while len(arr)>1:
            first=h.heappop(arr)
            second= h.heappop(arr)
            
            if first != second:
                h.heappush(arr,first-second)
                
        if len(arr)==1:
            return -h.heappop(arr)
        else:
            return 0
            
        
        
        