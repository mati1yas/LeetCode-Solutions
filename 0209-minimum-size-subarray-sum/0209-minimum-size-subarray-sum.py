class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        
        left=0
        right=0
        
        tot=0
        ans=float('inf')
        
        while right<len(nums):
            
            tot+=nums[right]
            
            while tot>=target:
                
                ans=min(ans,right-left+1)
                tot-=nums[left]
                left+=1
            
            right+=1
            
        
        return ans if ans !=  float('inf')  else 0
                
                