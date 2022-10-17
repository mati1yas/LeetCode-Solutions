class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return len(nums)
        
        rep=2
        
        for  i in range(2,len(nums)):
            
            if nums[i]!=nums[rep-2]:
                nums[rep]=nums[i]
                rep+=1
        return rep