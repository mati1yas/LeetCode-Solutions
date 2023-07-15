import heapq as h
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        
        ans=float('-inf')
        
        
        
        heap = []
        
        max_val=0
        for idx,(start,end,value) in enumerate(events):
            
            h.heappush(heap,(end,value))
            
            while heap and heap[0][0]<start:
                
                end,val=h.heappop(heap)
                
                max_val=max(max_val,val)
                
            ans=max(ans,max_val + value)
            
        return ans
                
                
                
                
                
                