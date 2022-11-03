class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        freq=defaultdict(int)
        
        count=0
        for word in words:
            
            freq[word]+=1
        
        foundCentral=False
        counted=set()
        for word in list(freq):
            
            if word[0]==word[1]:
                if freq[word]%2==0:
                    count+=freq[word]
                else:
                    count+=freq[word]-1
                    foundCentral=True
            elif word not in counted:
                count+=2*min(freq[word],freq[word[::-1]])
                counted.add(word)
                counted.add(word[::-1])
                
                
           
        if foundCentral:
            count+=1
        
        return count*2
        