class Solution:
    def simplifyPath(self, path: str) -> str:
        
        
        
        directories=path.split('/')
        
        
        stack=[]
        for dirc in directories :
            
            if dirc=="..":
                
                if stack :
                    stack.pop()
            
            elif dirc not in ('','.'):
                stack.append(dirc)
                
                
                
        return '/'+'/'.join(stack)