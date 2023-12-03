class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        canReach = [False ]* len(nums)
        
        
        
        canReach [-1] = True
        
        for i in range(len(nums)-1,-1,-1):
            
            for j in range(i, i+nums[i]+1):
                
                if canReach[j]==True:
                    canReach[i]=True
                    break
        return canReach[0]