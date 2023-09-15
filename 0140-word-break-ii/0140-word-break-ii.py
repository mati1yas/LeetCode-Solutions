class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
      
       
    
        canBeBroken=[False for _ in range(len(s)) ]
        canBeBroken.append(True)
        nextStart=defaultdict(list)
        for i in range(len(s)-1,-1,-1):
            
            
            for word in wordDict:
                if i+len(word)<len(canBeBroken) and word== s[i:i+len(word)] and canBeBroken[(i+len(word))]==True:
                    
                    nextStart[i].append((i+len(word),word))
                    canBeBroken[i]=True
                    
        
        ans=[]
        def backTrack (sentence, index):
            
            
            if index==len(canBeBroken)-1:
                ans.append(sentence)
                return 
            
            for nbr,word in nextStart[index]:
                space = ' ' if sentence else ""
                backTrack(sentence+space+word,nbr)
                
                
        backTrack("",0)
            
            
        return ans
                
                
                
                
                
                
                
                
                
            
            
        