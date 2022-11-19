class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        if len(nums)<3:
            return 0
        
        dp=[0]*len(nums)
        slices=0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                dp[i]=1+dp[i-1]
                slices+=dp[i]
                
        return slices