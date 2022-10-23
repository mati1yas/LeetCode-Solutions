class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
      
        last=defaultdict(int)
        left=0
        long=0
        right=0
        for right in range(len(s)):
            
            if s[right] in last  and left<=last[s[right]]:
                
               
                left=last[s[right]]+1
            else:
                 long=max(long,right-left+1)
                
                
            last[s[right]]=right
        
        
        return long