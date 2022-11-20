class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
        left=0
        right=0
        zeroes=0
        
        while right<len(nums):
            moved=False
            while right<len(nums) and nums[right]==nums[left]==0:
                right+=1
                moved=True
            n=right-left
            zeroes+=n*(n+1)//2
            if not moved:
                right+=1
            left=right
        return zeroes
            
            
            
        
        