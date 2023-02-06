class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        
        
        existingWords=set(words)
       
       
        self.memo={}
        def removeChar(word):
            
            if word in self.memo:
                
                return self.memo[word]
            
            
            localMax=1
            for i in range(len(word)):
                
            
                
                if word[:i]+word[i+1:] in existingWords:
                    
               
                    localMax=max(localMax,1+removeChar(word[:i]+word[i+1:]))
                
            
            self.memo[word]=localMax
            
                
            return localMax
            
            
        
        ans=1
        
        for word in words:
            ans=max(ans,removeChar(word))
            
        return ans