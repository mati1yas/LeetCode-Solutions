class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums)<2:
            return len(nums)
        
        
        curP=1
        
        for i in range(1,len(nums)):
            
            if nums[i]!=nums[curP-1]:
                nums[curP]=nums[i]
                curP+=1
            
        return curP