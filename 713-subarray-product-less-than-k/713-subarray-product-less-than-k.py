class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k<=1:
            return 0
        
        pro=1
        
        left=0
        answer=0
        for i in range(len(nums)):
            
            pro*=nums[i]
            
            while pro>=k:
                pro/=nums[left]
                left+=1
            
            answer+=i-left+1
            
        return answer
            