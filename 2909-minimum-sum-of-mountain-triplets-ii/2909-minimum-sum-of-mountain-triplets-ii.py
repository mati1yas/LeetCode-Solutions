class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        
        leftSmall=[nums[0]]*len(nums)
            
        rightSmall=[nums[-1]]*len(nums)
        
        
        
        for i in range(1,len(nums)):
            
            leftSmall[i]=(min(leftSmall[i-1],nums[i]))
            
        for i in range(len(nums)-2,-1,-1):
            rightSmall[i]=(min(rightSmall[i+1],nums[i]))
        
        ans=float('inf')
        for i in range(1,len(nums)-1):
            
            if nums[i]>leftSmall[i] and nums[i]>rightSmall[i]:
                ans=min(ans, leftSmall[i]+nums[i]+rightSmall[i])
            
        return -1 if ans==float('inf') else ans 
            
            
        