class Solution:
    
    def __init__(self):
        self.memo={}
    
    
    
    def diffWaysToCompute(self, expression: str) -> List[int]:    
        
        if expression in self.memo:
            
            return self.memo[expression]
        
        if expression.isdigit():
            
            self.memo[expression]=[int(expression)]
            return self.memo[expression]
        
            
        
        result=[]
        for i, char in enumerate(expression):
            
            if char in "+-*":
                
                left=self.diffWaysToCompute(expression[0:i])
            
                right=self.diffWaysToCompute(expression[i+1:])
                
                
                
#                 we are trying to get possible combinations of the left and right result
                for l in left:
                    for r in right:
                        
                        result.append(eval(str(l)+char+str(r)))
                        
                
        
        self.memo[expression]=result
        return result
                        
                        