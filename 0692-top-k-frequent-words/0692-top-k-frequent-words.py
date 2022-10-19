from collections import Counter
import heapq as h
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
                
        arr = [ (-count[x],x) for x in count.keys()]       
        
        h.heapify(arr)
        narr=[]
        
        while k>0:
            narr.append(h.heappop(arr))
            k-=1
               
        
#         print(narr6)
        # print(sorted(narr,key = lambda x:x[1]))
      
        
        return [j for i,j in narr]
        