class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanEquivalent={
            "M":1000,
            "CM":900,
            "D":500,
            "CD":400,
            "C":100,
            "XC":90,
            "L":50,
            "XL":40,
            "X":10,
            "IX":9,
            "V":5,
            "IV":4,
            "I":1
         }
            
         
       
        i=0
        ans=0
        while i < len(s):
            
#             let's first consider the big combinations 



            if i+1<len(s) and s[i:i+2] in romanEquivalent:
                
                ans+=romanEquivalent[s[i:i+2]]
                i+=2
                
        
            else:  # we consider one char roman number 
                
        
                ans+=romanEquivalent[s[i:i+1]]
                i+=1
                
        return ans
        
            
            
            
            
            
            