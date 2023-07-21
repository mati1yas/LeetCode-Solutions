class Solution:
    def calculate(self, s: str) -> int:
        
        
        stack=[]
        number=0
        symbol='+'
        s+='+'
        for char in s:
            
            if char==" ":
                continue
            
            if char.isdigit():
                number=number*10+int(char)
                
            else:
                
                if symbol=="+":
                    stack.append(number)
                    
                elif symbol=="-":
                    stack.append(-1*number)
                
                elif symbol=="*":
                    val=stack.pop()
                    stack.append(val*number)
                    
                elif symbol=="/":
                    val=stack.pop()
                    
                    stack.append(math.trunc(val/number))
                number=0
                symbol=char
                    
        return sum(stack)        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
    