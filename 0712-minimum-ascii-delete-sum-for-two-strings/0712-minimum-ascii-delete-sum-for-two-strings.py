class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
    
               
        
        
        
        memo = {}
        
        def deleteChar (pointer1,pointer2):
            
            
            if pointer1>len(s1)-1 and pointer2>len(s2)-1:
                return 0
            
            
            
            if (pointer1,pointer2) in memo:
                
                return memo[(pointer1,pointer2)]
            
            # cases 
            # 1. case one pointer ends first
            # 2. both not ended yet :
                 # 1. pointing to similar chars 
                    # move both both pointers without any cost  
                # 2.  different chars 
                      # 1 . delete left )_
                      # 2.  delete right 
                        # 3. delete both 
                
            if pointer1>len(s1)-1 and pointer2<=len(s2)-1:
                r=ord(s2[pointer2]) + deleteChar(pointer1,pointer2+1)
                memo[(pointer1,pointer2)]=r
                return r


            elif pointer1<=len(s1)-1 and pointer2>len(s2)-1:
                r=ord(s1[pointer1])+ deleteChar(pointer1+1,pointer2)
                memo[(pointer1,pointer2)]=r
                return r
            
            else:
                
                if s1[pointer1] == s2[pointer2]:
                    r=deleteChar(pointer1+1,pointer2+1)
                    memo[(pointer1,pointer2)]=r
                    return r
                
                else:
                    first= ord(s1[pointer1])+ deleteChar(pointer1+1,pointer2)
                    second=ord(s2[pointer2]) + deleteChar(pointer1,pointer2+1)
                    both=ord(s1[pointer1])+ord(s2[pointer2])+ deleteChar(pointer1+1,pointer2+1)
                    
                    memo[(pointer1,pointer2)]=min(first,second,both)
                    return min(first,second,both)
                
                    
        return deleteChar(0,0)
        