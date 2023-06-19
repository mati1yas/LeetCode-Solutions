class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        
        DIRS=[[1,0],[0,1],[-1,0],[0,-1]]
        mod = 10 ** 9 + 7
        memo=defaultdict(int)
        def inbound(row,col):
            
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        
        def dfs(row,col):
            
            if (row,col ) in memo:
                return memo[(row,col)]
            
            
            total=1
            for x, y in DIRS:
                nr,nc=row+x,col+y
                
                
                if inbound(nr,nc) and grid[nr][nc]<grid[row][col]:
                    
                    
                    total+=dfs(nr,nc)%mod
                    
            memo[(row,col)] = total
            return memo[(row,col)]
                    
                    
                    
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                ans+=dfs(i,j)
                    
                    
        return ans%mod
         
        
#         visited=set()
        
#         memo={}
#         def arithmetic_sum(n):
#             return (n * (n + 1)) // 2
#         def dp(row,col):
            
            
            
#             tot=1
#             for nbr in canGoto[(row,col)]:
                
#                 if nbr in memo:
#                     tot+=memo[nbr]
                    
#                 else:
#                     tot+=dp(nbr[0],nbr[1])
                    
            
#             memo[(row,col)]=math.factorial(tot)
            
#             return memo[(row,col)]
        
        
#         ans=0
#         print(canGoto)
#         for (x,y) in canGoto.copy().keys():
            
#             if (x,y) not in memo:
#                 print(x,y)
#                 ans+=dp(x,y)
                    
#         return ans