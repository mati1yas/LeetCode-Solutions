import heapq as h
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = [(a, b) for a, b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        
        minMultiplier=float('inf')
        ans=0
        total=0
        heap=[]
        for i in range(k):
            
            heap.append(pairs[i][0]) 
            minMultiplier=min(minMultiplier,nums2[i])
            total+=pairs[i][0]
        ans=total*pairs[k-1][1]
        
        h.heapify(heap)
        
       
        for i in range(k,len(nums1)):
            
            total+=pairs[i][0]
            
            num= h.heappop(heap)
            
            total-=num
            h.heappush(heap,pairs[i][0])
            ans=max(ans,total*pairs[i][1])
            
            
            
            
            
       
        
        return ans
            
            