class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        
        
        
        memo={}
        def dfs(index):
            
            
            if index>len(nums)-3:
                
                return 0
            
            if index in memo:
                return memo[index]
            
            
            
            first = max(0,k-nums[index])+dfs(index+1)
            second =  max(0,k-nums[index+1])+dfs(index+2)
            third = max(0,k-nums[index+2])+dfs(index+3)
            
            
            memo[index]= min(first,second,third)
            return memo[index]
        
        
        return dfs(0)