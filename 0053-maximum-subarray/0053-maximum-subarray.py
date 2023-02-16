class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        maxSub=0
        
        ans=float('-inf')
        for val in nums:
            if val>maxSub:
                if maxSub>=0:
                    maxSub+=val
                
                else:
                    maxSub=val
            else:
                maxSub+=val
                
            ans=max(ans,maxSub)
        
        
        return ans