import heapq as h
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        
        events.sort()
        
        
        
        
        heap=[]
        
        
        
        
        
        day=1
        
        count=0
        index=0
        
        
        for day in range(1,100000+1):
            
            
            while index<len(events) and events[index][0]==day:
                h.heappush(heap,events[index][1])
                index+=1
                
            
            
            while heap and heap[0]<day:
                
                
                h.heappop(heap)
                
            
            
            
            if heap:
                h.heappop(heap)
                
                count+=1
                
        return count
                
        
        
            
                
                
            
        
                

