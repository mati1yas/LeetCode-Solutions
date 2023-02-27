class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks=sorted(tasks,key= lambda task: -(task[1]-task[0]))
        def check(val):
            
            
            for a,b in tasks:
                
                if val>=b:
                    val-=a
                else:
                    return False
            if val>=0:
                return True
                
            
        actualSum=0
        estimatedSum=0
        
        for a, b in tasks:
            actualSum+=a
            estimatedSum+=b
        
        
        left = actualSum
        right = estimatedSum
        
        ans=float('inf')
        
        while left<=right :
            
            mid=(right+left)//2
           
            if check(mid):
                right=mid-1
                
                ans=min(ans,mid)
            else:
                left=mid+1
        return ans
            
            
                