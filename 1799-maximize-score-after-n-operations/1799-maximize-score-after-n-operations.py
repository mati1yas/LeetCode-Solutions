class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
   
        
        
        paired=set()
        
        self.memo={}
        def getScore(n,mask,):
            
            
            
            if n*2 == len(nums):
                return 0
            
            
            if mask in self.memo:
                return self.memo[mask]
            
            m = 0
            
            for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                    
                    if (mask>>i)&1 == 1 or (mask>>j)&1==1:  # is checking if either of them has been picked or not .
                        continue
                        
                        
                    newMask=mask|(1<<i)|1<<j  # marking the new  picked items


                    curVal=math.gcd(nums[i],nums[j])*(n+1)
                    m=max(m,getScore(n+1,newMask)+curVal)
                        
                    
            self.memo[mask]=m
            return m
                        
            
            
            
            
        m=0
        n=len(nums)//2
        
        mask  =  1<<len(nums)
        return getScore(0,mask)
            
            
            
            
            