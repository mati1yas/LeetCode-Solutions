class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        l1=list(s)
        l1.sort()
        
        l2=list(t)
        l2.sort()
        return l2==l1