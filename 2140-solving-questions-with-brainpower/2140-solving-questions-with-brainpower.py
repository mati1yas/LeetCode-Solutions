class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        
        
        
        
        
        self.memo={}

        def solveQuestion(current):
            
            if current >= len(questions):
                return 0 
            
            if current in self.memo:
                
                return self.memo[current]
            
            maxim= solveQuestion(current+1)   # not solve the current problem 
            skip=questions[current][1]+1
            point=questions[current][0]
            maxim = max(maxim, solveQuestion(current+skip)+point)
            
            self.memo[current]=maxim
            return maxim
        
        return solveQuestion(0)
            
            
            
            