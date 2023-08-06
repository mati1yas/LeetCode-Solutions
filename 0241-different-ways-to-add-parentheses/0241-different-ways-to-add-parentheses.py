class Solution:
    
    def __init__(self):
        self.memo={}
    
    
    
    def diffWaysToCompute(self, expression: str) -> List[int]:    
        
        if expression in self.memo:
            return self.memo[expression]
        
        if expression.isdigit():
            self.memo[expression]=[int(expression)]
            return self.memo[expression]
        
        res=[]
        for idx,char in enumerate(expression): 
            
            
            if char in '*-+':
                
                left = self.diffWaysToCompute(expression[:idx])
                right= self.diffWaysToCompute(expression[idx+1:])
                
                
                
                
                for leftVal in left:
                    for rightVal in right:
                        
                        res.append(eval(str(leftVal)+char+str(rightVal)))
                        
        self.memo[expression]=res  
        return res
                        
                        