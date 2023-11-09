class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        ans=0
        
        for i in range(len(nums)-2):
            
            
            max_=max(nums[i],nums[i+1],nums[i+2])
            
            if max_<k:
                
                c=k-max_
                
                nums[i]+=c
                nums[i+1]+=c
                nums[i+2]+=c
                
                ans+=c
        return ans
                