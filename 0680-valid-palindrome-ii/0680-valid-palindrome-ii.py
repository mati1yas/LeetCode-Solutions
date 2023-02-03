class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        
        
        left=0
        right=len(s)-1
        
        while left<=right:
            
            
            if s[left]!=s[right]:
#                 we check if delelting one of the characters gets us a  palindromic string 
                
                leftDeleted=s[0:left]+s[left+1:]
                rightDeleted=s[0:right]+s[right+1:]
            
                
                
                return leftDeleted==leftDeleted[::-1] or rightDeleted==rightDeleted[::-1]
            
            left+=1
            right-=1
            
        return True
        