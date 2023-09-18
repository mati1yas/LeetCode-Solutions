class Solution:
    def decodeString(self, s: str) -> str:
        # 2[ad4[af]]
        
        count= 0
        
        decoded =""
        
        
        stack =[]
        
        
        for ch in s:
            
            
            if ch.isdigit():
                
                count=10*count+int(ch)
                
            elif ch.isalpha():
                
                decoded+=ch
                
            elif ch  == "[":
                
                stack.append((count,decoded))
                
                decoded=""
                count=0
            elif ch== "]":
                prevcnt,prevDec=stack.pop()
                decoded= prevDec+prevcnt*decoded
        return decoded