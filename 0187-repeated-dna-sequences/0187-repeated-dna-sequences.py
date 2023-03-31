class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        
        left=0
        right=10
        
        ans=[]
        freq=defaultdict(int)
        while right <= len(s):
            
            
            substringBinary=0<<40
            
            for i, char in enumerate(s[left:right]):
                
                
                if char=="A":
                    
                    on=1<<i+31
                    
                    
                elif char=="C":
                    on=1<<i+21
                    
                    
                elif char=="G":
                    
                    on= 1<<i+11
                    
                    
                    
                elif char=="T":
                    on=1<<i
                substringBinary|=on
                
            if freq[substringBinary]==1 :
                ans.append(s[left:right])
                    
            freq[substringBinary]+=1
            
            
                    
            left+=1
            right+=1
            
            
        return ans
                    
            
                

            
        
        