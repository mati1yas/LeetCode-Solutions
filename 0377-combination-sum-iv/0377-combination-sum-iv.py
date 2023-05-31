class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        
        memo= {} 
        dp= [0 for _ in range(target+1)]
        dp[0]=1
        print(dp)
#         def dp(tar):
#             if tar==0:
#                 return 1
            
#             ways=0
#             if tar in memo:
                
#                 return memo[tar]
#             for val in nums:
                
#                 if tar-val>=0:
#                     ways+=dp(tar-val)
                    
#             memo[tar]= ways    
#             return ways
        
#         return dp(target)
                    
    
        for tar in range(1,target+1):
            
            for val in nums:
            
                if tar-val>=0:
                    
                    
                    
                    dp[tar]+=dp[tar-val]
                    
        return dp[-1]