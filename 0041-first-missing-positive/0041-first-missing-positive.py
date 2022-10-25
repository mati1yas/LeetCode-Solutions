class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        existing_nums=set(nums)
            
        for num in range(1,2**31-1):
            if num not in existing_nums:
                return num