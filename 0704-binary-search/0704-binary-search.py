class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        i=bisect.bisect_left(nums,target)
        
        
        
        if  i<len(nums) and nums[i]==target:
            return i
        else:
            return -1