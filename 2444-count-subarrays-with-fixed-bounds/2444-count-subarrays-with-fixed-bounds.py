
import heapq as h
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        
       
        
        left=0

        occurMin=-1
        occurMax=-1
        
        ans=0
        count=0
        for right in range(len(nums)):
            
            
            if nums[right]>maxK or nums[right]<minK:
                left=right+1
                occurMax=right
                occurMin=right
                
                
            else:
                
                if nums[right] == maxK:
                    occurMax=right
                if nums[right] == minK:
                    occurMin = right
                    
#                 valid subarrays
                
                if occurMax>=left and occurMin>=left:
                    count+=(min(occurMax,occurMin)-left+1)
                
                    
                    
                
                
            
            
            
            
            
        return count
            
                
                
                
                
            
            