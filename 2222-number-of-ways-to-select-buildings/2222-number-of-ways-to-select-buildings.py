class Solution:
    def numberOfWays(self, s: str) -> int:
        
        
        
        
        zeroes=0
        
        for char in s:
            if char=="0":
                zeroes+=1
            
        ones=len(s)-zeroes
        
        selection=0
        visitedOnes=0
        visitedZeroes=0
        if s[0]=="0":
            visitedZeroes+=1
        else:
            visitedOnes+=1
            
        
        for char in s[1:]:
            
            if char == "0":
                selection += visitedOnes*(ones-visitedOnes)
                visitedZeroes += 1
            
            else:
                selection +=visitedZeroes*(zeroes-visitedZeroes)
                visitedOnes +=1
                
        return selection
                