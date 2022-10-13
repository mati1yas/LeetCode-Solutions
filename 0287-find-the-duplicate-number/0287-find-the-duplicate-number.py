class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        arr=nums.copy()
        for n in nums:
            
            if arr[n-1]>=0:
                arr[n-1]*=-1
            else:
                return n
            