class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        
        
        while len(s)>k:
            
            
            tot=0
            ns=''
            
            for i in range(len(s)):
                if i%k==0 and i!=0:
                    ns+=str(tot)
                    tot=0
                tot+=int(s[i])
            
            s=ns+str(tot)
        print(s)
        return s