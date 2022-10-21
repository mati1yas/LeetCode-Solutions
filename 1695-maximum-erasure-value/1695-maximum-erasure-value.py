class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        
        
        lastIndex=defaultdict(int)
        
        left=0
        right=0
        pre=0
        maximum=0
        while right<len(nums):
            
            
            if nums[right] in lastIndex:
                maximum=max(maximum,pre)
               
                while left<=lastIndex[nums[right]]:
                    pre-=nums[left]
                    left+=1
            pre+=nums[right]
            lastIndex[nums[right]]=right
            right+=1
        maximum=max(maximum,pre)
                    
        return maximum
                