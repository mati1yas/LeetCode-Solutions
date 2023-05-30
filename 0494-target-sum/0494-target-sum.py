class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        
        memo = {}
        def recursive(total,i):
            
            
            
            if total==target and i>=len(nums):
                return 1
            if i>=len(nums):
                return 0
            
            if (total,i) in memo:
                
                return memo[(total,i)]
            
            
            take = recursive(total+nums[i],i+1)
            not_take= recursive(total-nums[i],i+1)
            
            
            memo[(total,i)] = take + not_take
            return take + not_take
        
        return recursive(0,0)
    