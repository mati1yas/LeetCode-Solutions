class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        
        
        dictionary_words=set(dictionary)
        
        
        def consider(start):
            
            
            r= float('inf')
            for end in range(start,len(s)):
                
                if s[start:end+1] in dictionary_words:
                    r=min(r,countExtras(end+1))

                


            return r
        memo={}
        def countExtras(index):
            
            
            if index==len(s):
                return 0
            
            
            if index in memo:
                
                return memo[index]
            
            isExtra=countExtras(index+1)+1  # consider this current char as extra
            
            
            notExtra  =  consider(index)
            
            memo[index]=min(notExtra,isExtra)
            return min(notExtra,isExtra)
        
        return countExtras(0)