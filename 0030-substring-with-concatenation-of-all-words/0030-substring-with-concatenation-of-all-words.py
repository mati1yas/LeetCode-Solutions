class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        
        
        
        wordLength= len(words[0])
        noOfWords=len(words)
        
        expectedLen=wordLength*(noOfWords)
        
        
        left=0
        right=expectedLen

        
        ans=[]
        
        while right<len(s):
            
            n=wordLength
            window=s[left:right]
            l=[window[i:i+n] for i in range(0, len(window), n)]
            
            if Counter(l)==Counter(words):
                ans.append(left)
                
           
            right+=1
            left+=1
        n=wordLength
        window=s[left:right]
        l=[window[i:i+n] for i in range(0, len(window), n)]
        
        if Counter(l)==Counter(words):
            ans.append(left)
            
        return ans
        
        