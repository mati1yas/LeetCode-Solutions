class Solution:
    def addMinimum(self, word: str) -> int:
        
        
        
        
        prev='z'
        sequence=0
        for char in word:
            
            if char <=prev:
                sequence+=1
            prev=char
        return sequence*3-len(word)
            
                
            