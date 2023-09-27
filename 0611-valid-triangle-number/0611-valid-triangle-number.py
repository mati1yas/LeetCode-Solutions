class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        
        
        nums.sort()
        
        count=0
        for i in range(len(nums)):
            first=nums[i]
            if not first:
                continue
            for j in range(i+1,len(nums)):
                
                second = nums[j]
                if not second :
                    continue
                
                left=bisect_left(nums,first+second)
                
                count+=left-j-1
                        
                
        return count
                
                
                