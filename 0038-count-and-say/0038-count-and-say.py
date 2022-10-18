class Solution:
    def countAndSay(self, n: int) -> str:
        
        
        def recount(n):
            if n==1:
                return "1"
            
            
            s=recount(n-1)
            rb=""            
            p1=0
            p2=0
            while p2<len(s):

                if s[p2]!=s[p1]:
                    rb+=str(p2-p1)+s[p1]
                    p1=p2
                p2+=1
            
            rb+=str(p2-p1)+s[p1]
           
            
            return rb
           
        return recount(n)
        