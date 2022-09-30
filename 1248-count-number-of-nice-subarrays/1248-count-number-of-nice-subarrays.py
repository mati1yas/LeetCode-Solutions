class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    
        
        queue=collections.deque()
        
        
        j=0
        i=0
        niceSubarrays=0
        while j <len(nums):
            
            if nums[j]%2!=0:
                queue.append(j)
            
            if len(queue)>k:
                
                while len(queue)>k:
                    
                    if nums[i]%2!=0:
                        queue.popleft()
                    
                    
                    i+=1
            j+=1
            
            if len(queue)==k:
                niceSubarrays+=queue[0]-i+1
                
        return niceSubarrays
            