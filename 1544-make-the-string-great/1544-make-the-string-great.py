class Solution:
    def makeGood(self, s: str) -> str:
        
        
        stack=[]
        
        for char in s:
            
            if char.isupper():
                if stack and stack[-1].islower():
                    if char.lower()==stack[-1]:
                        stack.pop()
                        continue
                        
            if char.islower():
                if stack and stack[-1].isupper():
                    if char.upper()==stack[-1]:
                        stack.pop()
                        continue
            stack.append(char)
            

        return ''.join(stack )