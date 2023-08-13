class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        
        
        
        n=len(nums)
        
        
        memo={-1:True}
        def validatePrefix(index):
            
            
            
            
            if index in memo:
                return memo[index]
            
            
            isValid=False
            
            
            if index>0 and nums[index] == nums[index-1]:
                
                isValid|=validatePrefix(index-2)
                
            if index>1 and nums[index]==nums[index-1]==nums[index-2]:
                
                isValid|=validatePrefix(index-3)
                
            if index>1 and nums[index]==nums[index-1]+1==nums[index-2]+2:
                isValid|=validatePrefix(index-3)
            memo[index]=isValid 
            return isValid
        
        return validatePrefix(n-1)
            
            