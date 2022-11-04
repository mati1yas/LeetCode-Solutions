class Solution:
    def reverseVowels(self, s: str) -> str:
        
        
        letters=list(s)
        
        left=0
        right=len(s)-1
        
        while left<=right:
            
            while left< right and letters[left] not in "aeiouAEOIU":
                left+=1
            while left<right  and letters[right] not in "aeiouAEOUI":
                right-=1
            
            letters[left],letters[right]=letters[right],letters[left]
            left+=1
            right-=1
        
        return ''.join(letters)
            