class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=""
        
        letters=[]
        
        for char in s:
            letters.append(char)
            if char in 'auieoAEOIU':
                vowels=char+vowels
        
        p=0
        
        for idx,char in enumerate(letters):
            
            if char in "auieoAEOIU":
                letters[idx]=vowels[p]
                p+=1
        return ''.join(letters)