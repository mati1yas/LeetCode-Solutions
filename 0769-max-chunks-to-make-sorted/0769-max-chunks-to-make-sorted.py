class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        
        stack  = []
        
        
        for num in arr:
            
            rep=num
            
            while stack and stack[-1]>num:
                rep=max(rep,stack.pop())
                
            stack.append(rep)
            
            
        return len(stack)
            
        
            
    