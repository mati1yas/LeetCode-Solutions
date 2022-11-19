class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s)==0:
            return True
        
        p1=0
        p2=0
        
        while p2<len(t):
            
            if t[p2]==s[p1]:
                p1+=1
            p2+=1
            if p1==len(s):
                return True
        
        return False