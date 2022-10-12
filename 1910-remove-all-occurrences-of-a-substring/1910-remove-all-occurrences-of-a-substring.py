class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack =[]
        k=len(part)
        for i in range(len(s)):
            stack.append(s[i])
            
            while len(stack)>=k and stack[-k:]==list(part):
                
                for i in range(k):
                    stack.pop()
                    
        return ''.join(stack)