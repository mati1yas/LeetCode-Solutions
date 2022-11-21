class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        
        if len( nums)==1:
            return 1
        length= 1 if nums[1]==nums[0] else 2
        
        prevDiff=nums[1]-nums[0]
        
        for i in range(2,len(nums)):
            
            if ( nums[i]-nums[i-1]>0 and prevDiff<=0 )or (nums[i]-nums[i-1]<0 and prevDiff>=0):
                length+=1
                prevDiff=nums[i]-nums[i-1]
        
        return length