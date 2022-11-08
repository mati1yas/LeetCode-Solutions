import heapq as h
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # the main reason i wanted heap for is to get minimum ugly 
        
        
        heap=[]
        h.heappush(heap,1)
        generated=set({1})
        
        res=[]
        for i in range(1,1691):
            
            ugly=h.heappop(heap)
            res.append(ugly)
            for prime in [2,3,5]:
                
                newUgly=prime*ugly
                
                if newUgly not in generated:
                    generated.add(newUgly)
                    h.heappush(heap,newUgly)
        
                    
        return res[n-1]