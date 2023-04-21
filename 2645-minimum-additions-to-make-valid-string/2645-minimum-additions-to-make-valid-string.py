class Solution:
    def addMinimum(self, word: str) -> int:
        
        
        
#          the main idea of this approach is to count how many increasing sequence we have 

#         if we get decreasing it means we have to start a new sequence 
        prev='z'
        sequence=0
        for char in word:
            
            if char <=prev:
                sequence+=1
            prev=char
        return sequence*3-len(word)
            
                
            