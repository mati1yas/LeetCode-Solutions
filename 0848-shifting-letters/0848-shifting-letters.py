class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        
        
        prefix=[]
        
        for shift in shifts[::-1]:
            
            if prefix :
                prefix.insert(0,prefix[0]+shift)
            else:
                prefix.insert(0,shift)
                
        
        ns=''
        for i, char in enumerate(s):
            
            val = ord(char)
            pre=prefix[i]%26
            if val+pre>ord('z'):                
                dif = ord('z')-val                
                ns+= chr (ord('a')+pre-dif-1)
            else:
                ns+=chr(val+pre)
                
        return ns
            
            