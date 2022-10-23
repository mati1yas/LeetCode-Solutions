class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        
        start=0
        end=0
        long=0
        collected=0
        while end<len(nums):
            
            while collected & nums[end]!=0:
                
                collected ^= nums[start]
                start+=1
            long=max(long,end-start+1)
            collected|=nums[end]
            end+=1
        return long