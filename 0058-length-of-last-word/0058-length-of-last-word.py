class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        l=s.split(' ')
        
        
        words=[]
        
        for word in l:
            if word != "":
                words.append(word)
        return len(words[-1])

