class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        ans=[-1 for i in range(len(nums))]
        
        if len(nums)<(2*k)+1:
            return ans
        
        
        right=0
        left=0
        
        tot=0
        index=k
        while right<len(nums):
            
            
            while right<len(nums) and  right-left+1<=(2*k)+1:
                tot+=nums[right]
                
                right+=1
            window=right-left
        
            ans[index]=tot//window
            index+=1
            tot-=nums[left]
            left+=1
            
        return ans
        