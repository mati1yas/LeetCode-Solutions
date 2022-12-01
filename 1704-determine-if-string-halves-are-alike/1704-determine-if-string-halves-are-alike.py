class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        
        countLeft=0
        half=len(s)//2
        vowels=set({'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'})
        for char in s[:half]:
            if char in vowels:
                countLeft+=1
                
                
        countRight=0  
        for char in s[half:]:
            
            if char in vowels:
                countRight+=1
            
        return countLeft==countRight