class Solution:    
    
    
    def numTrees(self, n: int) -> int:
        
        
        dp=[0]*(n+1)
#         for these two cases we can only form one bst for each
        dp[0]=1  
        dp[1]=1
#          this is called catalan number 
        for i in range(2,n+1):
            
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
                
        return dp[n]