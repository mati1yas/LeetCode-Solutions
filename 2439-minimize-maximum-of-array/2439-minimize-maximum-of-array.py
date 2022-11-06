class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        result=0
        cursum=0
        for i , num in enumerate(nums,start=1):
            cursum+=num
            
            result=max(math.ceil(cursum/i),result)
            
        
        
        return result