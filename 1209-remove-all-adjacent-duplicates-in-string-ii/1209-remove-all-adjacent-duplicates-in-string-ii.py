class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack=[]
        
        for char in s:
            
                         
            if stack and stack[-1][0]==char:
                char,freq=stack.pop()
                stack.append((char,freq+1))
                
            else:
                stack.append((char,1))
            
            if stack[-1][1]==k:
                stack.pop()
                         
                         
            
                    
    
        newS=""
        for char,freq in stack:
            newS+=char*freq
        return newS
        
        print(stack)