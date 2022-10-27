class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        memo=defaultdict(int)
        points=defaultdict(int)
        large=0
        for num in nums:
            
            points[num]+=num
            if num>large:
                large=num
    
        def maxPoints(num):
            
            if num==0:
                return 0
            if num==1:
                return points[1]
            
            
            # we create recurrence relation here 
            if num not in memo:
                
                memo[num]=max(maxPoints(num-2)+points[num],maxPoints(num-1))
            
            return memo[num]
        
        return maxPoints(large)
        