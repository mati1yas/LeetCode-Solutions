class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        r=[-1]*len(nums)
        for i in range(len(nums)):
            
            for j in range(i+1,len(nums)+i):
                
                curidx=j%len(nums)
                
                if nums[curidx]>nums[i]:
                    
                    r[i]=nums[j%len(nums)]
                    break
            
        return r