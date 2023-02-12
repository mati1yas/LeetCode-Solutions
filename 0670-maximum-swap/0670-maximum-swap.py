class Solution:
    def maximumSwap(self, num: int) -> int:
        
        
        s=list(str(num))
        
        ans=s[:]
        
        
        for i in range(len(s)):
            for j in range(i+1,len(s)):
            
                s[i],s[j]=s[j],s[i]
                
                if int("".join(s))>int("".join(ans)):
                    ans=s[:]
                    
                s[i],s[j]=s[j],s[i]
                
        
        return int("".join(ans))
                
        