class Solution:
    def isValid(self, s: str) -> bool:
        
        
        stack=[]
        
        
        stack=[]
        
        closing={
            "}":"{",
            "]":"[",
            ")":"("
        }
        
        for char in s:
            

            if char in "}])" and not stack:
                return False
            elif char in "}])"  and closing[char]!=stack[-1] :
                return False
            elif char in "[{(":
                stack.append(char)
            else:
                stack.pop()
                
            
                
        return not stack   
       