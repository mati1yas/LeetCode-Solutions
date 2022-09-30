class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        
        
        
        
        
        
        d=defaultdict(int)
        d[0]=1
        
        presum=0
        answer=0
        for num in nums:
            presum+=num
            answer+=d[presum-k]
            
            d[presum]+=1
        return answer
            
            