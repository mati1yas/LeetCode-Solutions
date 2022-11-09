class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        
        
        
        
        rank=set()
        visited=set()
        def permutate(newS,index):
            rank.add(newS)
            if newS in visited:
                return 
            for idx in range(index,len(s)):
                
                if s[idx].isalpha():
                    permutate(newS,index+1)
                    np=newS[:idx]+newS[idx].swapcase()+newS[idx+1:]
                    permutate(np,index+1)
                    visited.add(np)
                    visited.add(newS)
                    
                    
                
                
            
            
            
        
        
        permutate(s,0)
            
        return list(rank)
            
        
        
        