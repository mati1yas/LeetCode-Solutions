class Solution:
    def addMinimum(self, word: str) -> int:
        
        
        
        count=0
        i=0
        while i<len(word):
            
            for char in 'abc':
                if i<len(word) and char == word[i]:
                    i+=1
                else:
                    count+=1
        
        return count
                    
                    
        
                
            