class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        
        
        
        values= [ (nums[i],cost[i]) for i in range(len(nums))]
        
    
        
        def calCost(change):
            tot = 0
            
            for n,c in values:
                tot+=abs(n-change)*c 
                
            
            return tot
        
        
        
        
        left=min(nums)
        
        right=max(nums)
        
        ans=calCost(left)
        while left<=right:
            
            mid= (right+left)//2
            
            cost1 = calCost(mid)
            cost2 = calCost(mid+1)
            ans=min(cost1,cost2)
            
            if cost1>cost2:
                left=mid+1
            else:
                right=mid-1
        return ans
        
            
            