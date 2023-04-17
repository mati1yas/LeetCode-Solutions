class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        
        
        def divide(slicedString):
            
            
            if len(slicedString)<k:
                return 0
            
            
            freq=Counter(slicedString)
            
            
            for idx,char in enumerate(slicedString):
                
                
                if freq[char]<k:
                    
                    return max(divide(slicedString[:idx]),divide(slicedString[idx+1:]))
                
            
            return len(slicedString)
        
        return divide(s)
                
                
            
            
            
            
            
            