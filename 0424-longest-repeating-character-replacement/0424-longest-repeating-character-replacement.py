class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        freq=defaultdict(int)
        long=0
        left=0
        
        for right in range(len(s)):
            
            
            window=right-left+1
            freq[s[right]]+=1
            
            while window-max(freq.values())>k:
                freq[s[left]]-=1
                left+=1
                window=right-left+1
            
            long=max(window,long)
            
        return long
        
