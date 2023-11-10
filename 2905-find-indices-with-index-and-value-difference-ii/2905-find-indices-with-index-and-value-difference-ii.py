class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        
        
        mini=0
        maxi=0
        
        d= indexDifference
        
        for i in range(d,len(nums)):
            
            
            if nums[i-d]<nums[mini]:
                mini=i-d
            
            if nums[i-d]>nums[maxi]:
                maxi=i-d
                
                
            if abs(nums[mini]-nums[i])>=valueDifference:
                return [mini,i]
            
            if abs(nums[maxi]-nums[i])>=valueDifference:
                return [maxi,i]
            
            
        return [-1,-1]