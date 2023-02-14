class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        if n==1:
            return [0]
        
        
        ans=[]
        i=1
        while len(ans)<=n-2:

            ans.append(i)
            ans.append(-1*i)
            i+=1
        if n%2==0:
            return ans
            
            
        
        else:
            ans.append(0)
            return ans
            