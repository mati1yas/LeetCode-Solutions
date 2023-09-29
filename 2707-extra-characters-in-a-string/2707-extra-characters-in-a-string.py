class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        
        
        dictionary_words=set(dictionary)
        
        
        self.memo={}
        
        def partOfString (start):
            
            
            
            r=float('inf')
            
            
            for end in range(start, len(s)):
                
                
                if s[start:end+1]  in dictionary_words:
                    
                    r=min(r,countExtras(end+1))
            
            return r
            
            
        
        
        
        def countExtras(index):
            
            if index>=len(s):
                return 0
            
            if index  in self.memo:
                return self.memo[index]
            
            
            considerItExtra=countExtras(index+1)+1
            
            considerNotExtra=partOfString(index)
            
            self.memo[index]=min(considerItExtra,considerNotExtra)
            return self.memo[index]
        
        
        return countExtras(0)
            
            
            
            
            