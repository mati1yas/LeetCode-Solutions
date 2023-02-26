class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        
        
        
        prevArthimetics=defaultdict(int)
                
        
        for i in range(len(nums)):
            
            for j in range(i):
                
                diff=nums[i]-nums[j]
                
                prevArthimetics[(i,diff)]=prevArthimetics[(j,diff)]+1
                
        
        return max(prevArthimetics.values())+1
                