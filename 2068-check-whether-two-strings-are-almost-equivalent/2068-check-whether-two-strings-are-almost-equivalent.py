class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1=Counter(word1)
        freq2=Counter(word2)
                
                
                
        
        
        for let in freq1:
            
            if abs(freq1[let]-freq2[let])>3:
                return False
        for let in freq2:
            
            if abs(freq1[let]-freq2[let])>3:
                return False
        return True