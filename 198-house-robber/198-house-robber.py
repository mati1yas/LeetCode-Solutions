class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        self.maxrob=0
        memo={}
        def robber(i):
            
            
            if i>=len(nums):
                return 0
            robbed=0
            for x in range(i+2,len(nums)):
                if x in memo:
                    r=memo[x]
                else:
                    r=robber(x)
                robbed=max(r,robbed)
            
            memo[i]=robbed+nums[i]
            
            return memo[i]
                
            
        for i in range(len(nums)):
            
            if i in memo:
                self.maxrob=max(self.maxrob,memo[i])
                continue
            self.maxrob=max(self.maxrob,robber(i))
        return self.maxrob
            