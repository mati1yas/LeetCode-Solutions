class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        
        
        
        if expression.isdigit():
            return [int(expression)]
        
            
        
        result=[]
        for i, char in enumerate(expression):
            
            if char in "+-*":
                
                left=self.diffWaysToCompute(expression[0:i])
            
                right=self.diffWaysToCompute(expression[i+1:])
                
                for l in left:
                    for r in right:
                        
                        result.append(eval(str(l)+char+str(r)))
                        
                
        
        return result
                        
                        