class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        freq1=Counter(word1)
        freq2=Counter(word2)
        
        
        
        freq1=list(freq1.values())
        freq2=list(freq2.values())
        freq1.sort()
        freq2.sort()
        
        return freq1==freq2 and set(word1)== set(word2)