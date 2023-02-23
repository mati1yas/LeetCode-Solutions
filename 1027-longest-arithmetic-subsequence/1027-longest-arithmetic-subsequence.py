class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        
        freq=defaultdict(int)
        
        for i in range(1,len(nums)):
            
            for j in range(i):
                diff=nums[i]-nums[j]
                
                freq[i,diff]=freq[j,diff]+1
                
        
        return max(freq.values())+1
                
                