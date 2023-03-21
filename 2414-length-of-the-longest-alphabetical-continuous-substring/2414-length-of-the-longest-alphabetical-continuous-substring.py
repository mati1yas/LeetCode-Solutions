class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        
        
        ans=0
        count=1
        right=0
        while right < len(s):
            
            if right and s[right]>s[right-1] and ord(s[right])-ord(s[right-1])==1:
                count+=1
            else:
                
                ans=max(ans,count)
                count=1
            right+=1
                
                 
        ans=max(ans,count)
        return ans