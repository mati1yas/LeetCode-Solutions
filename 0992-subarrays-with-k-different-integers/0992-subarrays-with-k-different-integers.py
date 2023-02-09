class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        
        distinctChars=defaultdict(int)
        
        
        
        left=0
        right=0
        res=0

        while right<len(nums):
            
            distinctChars[nums[right]]+=1
            
            
            while len(distinctChars)>k:

                distinctChars[nums[left]]-=1

                if distinctChars[nums[left]]==0:
                    distinctChars.pop(nums[left])

                left+=1
                    
            res+=right-left+1
                
            right+=1

        left=0
        right=0
        res2=0

        distinctChars=defaultdict(int)
        while right<len(nums):
            
            distinctChars[nums[right]]+=1
            
            
            while left<len(nums) and len(distinctChars)>k-1:

                distinctChars[nums[left]]-=1

                if distinctChars[nums[left]]==0:
                    distinctChars.pop(nums[left])

                left+=1
                    
            res2+=right-left+1
                
            right+=1
            
            
        return res-res2
            
            
            
            
            