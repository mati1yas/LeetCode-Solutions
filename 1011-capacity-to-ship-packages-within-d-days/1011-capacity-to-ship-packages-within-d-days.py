class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        left=max(weights)
        right=sum(weights)
        
        
        def calculate(mid):
            calcDays=1
            tot=0
            for w in weights:
                
                if tot+w<=mid:
                    tot+=w
                else:
                    tot=w
                    calcDays+=1
            return calcDays
       
        
        minDays=0
        while left<=right:
            
            mid=(left+right)//2
            calcDays=calculate(mid)
           
            if calcDays<=days:
                right=mid-1
                minDays=mid
            
            else:
                left=mid+1
        
        return minDays
            
                