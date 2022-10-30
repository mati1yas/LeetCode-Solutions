class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        if 0 in nums:
            return len(set(nums))-1
        else:
            return len(set(nums))