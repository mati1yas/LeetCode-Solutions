class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n=0
        
        for  i, num in enumerate(nums):
            n = n^num^i
        
        return n^(i+1)
            