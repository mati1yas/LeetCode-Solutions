class Solution:
    def integerReplacement(self, n: int) -> int:
        
        
        self.operations=float('inf')
        def dfs(num,op):
            if op>=self.operations:
                return
            if num==1:
                self.operations=min(self.operations,op)
                return 
            if num<=0:
                return 
            if num%2==0:
                dfs(num//2,op+1)
            else:
                dfs(num-1,op+1)
                dfs(num+1,op+1)
            
            
        
        dfs(n,0)
        return self.operations