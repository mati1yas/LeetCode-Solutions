class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        left=0
        right=0
        
        vowels=set({'a','e','i','u','o'})
       
        countVowels=0
        maximumVowels=0
        while right<len(s):
            
            
            while right-left<k:
                
                if s[right] in vowels:
                    countVowels+=1
                right+=1
            
            maximumVowels=max(maximumVowels,countVowels)
            if s[left] in vowels:
                countVowels-=1
            left+=1
        return maximumVowels