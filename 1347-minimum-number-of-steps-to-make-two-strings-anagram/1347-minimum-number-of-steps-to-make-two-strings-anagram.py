class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        
        sCounts=Counter(s)
        
        tCounts=Counter(t)
        
        replacement=0
        for char in t:
            
            if sCounts[char]>=1:
                sCounts[char]-=1
                
            else:
                replacement+=1
        return replacement