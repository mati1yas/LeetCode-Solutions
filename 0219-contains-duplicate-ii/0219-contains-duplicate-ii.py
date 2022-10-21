class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        
        
        lastIndex={}
        
        end=0
        
        while end<len(nums):           
                       
            
            if  nums[end] in lastIndex and abs(end-lastIndex[nums[end]])<=k:
                
                return True
            
            
            lastIndex[nums[end]]=end
            end+=1
        
        return False