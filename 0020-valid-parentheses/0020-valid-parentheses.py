class Solution:
    def isValid(self, s: str) -> bool:
        
        

        
      
    
        openings='([{'
        closings=')}]'
        matches={
            ')':'(',
            ']':'[',
            '}':'{',
        }
        
        stack = [ ]
        for char in s:
            
            
            
            if char in openings:
                stack.append(char)
                
            elif char in closings:
                if not stack:
                    return False
                if matches[char]!=stack[-1]:
                    return False
                else:
                    stack.pop()
                    
        
                    
        return stack==[]
                    
            
            
            