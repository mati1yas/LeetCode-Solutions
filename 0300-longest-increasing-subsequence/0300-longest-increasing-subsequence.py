class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        
        dp=[1]* len(nums)
        
        
        long=1
        for i in range(1,len(nums)):
            
            for j in range(i):
                
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
            
            long=max(long,dp[i])
            
        
        return long