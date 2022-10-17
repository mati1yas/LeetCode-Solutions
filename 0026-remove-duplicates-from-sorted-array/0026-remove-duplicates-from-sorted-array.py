class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums)<2:
            return len(nums)
        
        rep=1
        for  i in range(1,len(nums)):
            
            if nums[i]!=nums[rep-1]:
                nums[rep]=nums[i]
                
        
                rep+=1
            
        return rep