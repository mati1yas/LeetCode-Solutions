class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        
        
        
        heap=[]
        
        
        ans=0
        
        max_val=0
        ans=0
        for idx,(start,end , value) in enumerate(events) :
            heapq.heappush(heap,(end,value))
            
            while heap and heap[0][0]<start:
                
                end2,val = heapq.heappop(heap)
                
                max_val= max(max_val,val)
            
            ans=max(ans,max_val+value)
            
            
        return ans