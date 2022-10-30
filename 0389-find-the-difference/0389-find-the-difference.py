class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        freqS=Counter(s)
        freqT=Counter(t)
        
        
        for char in t:
            if freqS[char] != freqT[char]:
                return char
        