class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        
        
        arr=list(set(nums))
        arr.sort()
        
        
        if len(arr)<3:
            return max(arr)
        
        return arr[-3]