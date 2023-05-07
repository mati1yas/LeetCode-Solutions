class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        
        
        nums.sort()
        
        count=0
        for i in range(len(nums)):
            
            
                
           
            leftB=bisect_left(nums,lower-nums[i])
            rightB=bisect_right(nums,upper-nums[i])
            
            
            leftB=max(i+1,leftB)
            
            if rightB > i:
                
                count+=rightB-leftB
            
            
        return count
            