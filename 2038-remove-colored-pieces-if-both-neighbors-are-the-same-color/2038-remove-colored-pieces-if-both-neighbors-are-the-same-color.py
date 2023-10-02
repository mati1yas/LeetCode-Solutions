class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        
        stack = []
        
        
        alice = 0
        bob = 0
        for char in colors:
            
            if stack and stack[-1][0]==char:
                
                if stack[-1][1]==2:
                    if char=="A":
                        alice+=1
                    else:
                        bob+=1
                else:
                    stack[-1][1]+=1
            else:
                stack.append([char,1])
                
        if alice>bob:
            return True
        else:
            return False
                    
                
            
            
            