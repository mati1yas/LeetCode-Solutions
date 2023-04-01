class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        
        next_hotter=[0 for i in range(len(temperatures))]
        
        
        stack=[]
        for idx,temp in enumerate(temperatures):
            
            
            while stack and stack[-1][1] < temp:
                topInd,topT=stack.pop()
                
                next_hotter[topInd]=idx-topInd
                
            stack.append((idx,temp))
            
        return next_hotter