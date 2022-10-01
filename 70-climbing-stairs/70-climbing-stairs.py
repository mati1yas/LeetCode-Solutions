class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        if n==1:
            return 1
        self.ways={}
        def dfs(i):
            if i==n or i==n-1:
                
                return 1
            if i>n:
                return 0
            
            ways=0
            for x in range(1,2+1):
                ni=x+i
                
                if ni<n+1:
                    if ni in self.ways:
                        ways+=self.ways[ni]
                    else:
                        ways+=dfs(ni)
            
            self.ways[i]=ways
            return ways
                
        
        dfs(0)
        
        return self.ways[0]    
            