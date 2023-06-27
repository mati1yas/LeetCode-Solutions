import heapq as h
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        

        
        can=candidates
        
        left=0
        right=len(costs)-1
        
        heap=[]
        
        visited=set()
        
        while can:
            h.heappush(heap,(costs[left],left))
            can-=1
            visited.add(left)
            left+=1
        can= candidates
        while can:
            
            if right not in visited:
                h.heappush(heap,(costs[right],right))
            can-=1
            right-=1
            
                
      
              
        right=right+1
        left-=1
            
    
        total=0
        
        while k:
            cost,index=h.heappop(heap)
            if left+1<right:
                if index<=left:

                    left+=1
                    h.heappush(heap,(costs[left],left))
                elif index>=right:
                    right-=1
                    h.heappush(heap,(costs[right],right))
           
            total+=cost
            k-=1
        return total
        
            
            
            
            
            
            
        
        