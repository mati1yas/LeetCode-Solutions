class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        
        
        #this is will find the duplicate 
        
        nums.sort()
        duplicate=None
        found=set()
        for num in nums:
            if num in found:
                duplicate=num
            found.add(num)
        
        existing=set(nums)
        # herer we will find the missing number
        missing=None
        for num in range(1,len(nums)+1):
            if num not in existing:
                missing=num
        
        return [duplicate,missing]