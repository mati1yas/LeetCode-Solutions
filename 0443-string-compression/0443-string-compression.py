class Solution:
    def compress(self, chars: List[str]) -> int:
        
        
        left=0
        right=0
        
        
        
        curFreq=1
        curChar=chars[0]
        chars+=" "
        for right in range(1,len(chars)):
            
            if chars[right]==curChar:
                curFreq+=1
            
            elif  chars[right]!=curChar:
                
                c=0
                
                chars[left]=curChar
                
                left+=1
                if curFreq>1:
                
                    
                    while  c<len(str(curFreq)):
                        chars[left]=str(curFreq)[c]
                        left+=1
                        c+=1
                
                    
                
                
                
                curChar=chars[right]
                curFreq=1


        return left
        