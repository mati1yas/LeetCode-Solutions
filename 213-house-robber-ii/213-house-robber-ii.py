class Solution:
    
    def helper(self,arr):
        
        self.maxrobbed=0
        memo={}
        
        def robber(i):
            
            if i>=len(arr):
                return 0
            
            robbed=0
            
            for x in range(i+2,len(arr)):               
                
                if x not  in memo:
                    
                    r=robber(x)
                else:
                    r=memo[x]
                robbed=max(r,robbed)
               
            memo[i]=robbed+arr[i]
            
            return memo[i]
            
           
        for i in range(len(arr)):
            
            if i in memo:
                self.maxrobbed=max(self.maxrobbed,memo[i])
                continue

            self.maxrobbed=max(self.maxrobbed,robber(i))
        return self.maxrobbed
                
        
    
    
    
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
        
        
        
        
        
        
          
        
        
        
        