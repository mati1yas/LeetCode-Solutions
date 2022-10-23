class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        
        
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
            
        ans=0
        
        
        for num in freq:
            
            if k==0 and freq[num]>1:
                ans+=1
                
            elif k>0 and num+k in freq:
                
                ans+=1
        
        return ans