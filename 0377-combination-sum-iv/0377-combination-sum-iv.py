class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        memo= {} 
        
        
        def dp(tar):
            
            
            
            if tar==0:
                return 1
            
            ways=0
            
            if tar in memo:
                
                return memo[tar]
            for val in nums:
                
                if tar-val>=0:
                    ways+=dp(tar-val)
                    
            memo[tar]= ways    
            return ways
        
        return dp(target)
                    