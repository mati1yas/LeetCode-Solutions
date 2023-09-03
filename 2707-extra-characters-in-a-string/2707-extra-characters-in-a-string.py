class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        
        
        dictionary_words=set(dictionary)
        
        
        def canBeBuilt(start):
            
            
            r= float('inf')
            for end in range(start,len(s)):
                
                if s[start:end+1] in dictionary_words:
                    r=min(r,buildSub(end+1))

                


            return r
        memo={}
        def buildSub(index):
            
            
            if index==len(s):
                return 0
            
            
            if index in memo:
                
                return memo[index]
            
            notTake=buildSub(index+1)+1
            
            
            take=  canBeBuilt(index)
            
            memo[index]=min(notTake,take)
            return min(notTake,take)
        
        return buildSub(0)