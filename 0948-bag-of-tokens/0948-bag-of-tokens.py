class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        
        
        
        tokens.sort()
        
        left = 0
        right = len(tokens)-1
        
        
        score= 0 
        ans=0
        
        while left <= right :
            
            if power>=tokens[left]:
                
                
                
                score+=1
                
                ans=max(ans,score)
                
                power-=tokens[left]
                left+=1
                
            elif power<tokens[left] and score:
                
                score-=1
            
                power+=tokens[right]
                right-=1
                
            else:
                return ans
            
        
        return ans
                
        
        
        
        
        