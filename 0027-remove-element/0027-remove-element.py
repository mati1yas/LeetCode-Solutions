class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        left=0
        right=len(nums)-1
        
        while left<right:
            
            while left<right and nums[left]==val:
                nums[right],nums[left]=nums[left],nums[right]
                right-=1
            left+=1
                  
            
        
        return len(nums)-Counter(nums)[val]