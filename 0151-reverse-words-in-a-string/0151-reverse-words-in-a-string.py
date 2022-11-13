class Solution:
    def reverseWords(self, s: str) -> str:
        
        ns=[]
        
        for word in s.split(' ')[::-1]:
            
            if word:
                ns.append(word)
            
        return ' '.join(ns)