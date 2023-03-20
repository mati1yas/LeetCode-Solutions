class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack=[]
        for ast in asteroids:
            
            
            op=False
            
            while stack and (stack[-1]>0  and ast<0 ) :
                
                if abs(stack[-1])<abs(ast): # top is gonna explode
                    stack.pop()
                    continue
                    
                elif abs(stack[-1])==abs(ast): # both explode
                    stack.pop()
                    
                    op=True
                    break
                else:      
                    # right explodes
                    op=True
                    break
                    
            if not op:
                stack.append(ast)
                    
                    
                    
                    
            
        
        return stack
                