class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        
        def digitSum(n):
            tot=0
            while n:
                rem=n%10
                
                tot+=rem
                n=n//10
                
            
            
            
            return tot
    
        grps=defaultdict(int)
        
        
        for i in range(1,n+1):
            digitsum=digitSum(i)
            grps[digitsum]+=1
        
        
        largest=Counter(grps.values())
        
        return largest[max(grps.values())]
        
            
         