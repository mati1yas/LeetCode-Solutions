class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        
        
        
        
        maxSofar=nums[0]
        maxEnding=nums[0]
        
        
        
        minSofar = nums[0]
        minEnding = nums[0]
        
        
        total=nums[0]
        
        
        for i in range(1,len(nums)):
            
            maxEnding=max(0,maxEnding)+nums[i]            
            maxSofar=max(maxSofar,maxEnding)   
            
            total+=nums[i]
            
            minEnding=min(0,minEnding)+nums[i]           
            minSofar=min(minSofar,minEnding)
        
        if total==minSofar:
            return maxSofar
        
        return max(maxSofar,total-minSofar)