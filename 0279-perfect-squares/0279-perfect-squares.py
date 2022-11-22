class Solution:
    def numSquares(self, n: int) -> int:
        
        perfectSquares=[]
        for i in range(1,n+1):
            if i**(.5) == int(i**(.5)):
                perfectSquares.append(i)
            
        
        
        queue=collections.deque()
        visited=set({(n,0)})
        
        queue.append((n,0))
        while queue:
            
            cur,steps=queue.popleft()
            
            for per in perfectSquares:
                
                if cur-per==0:
                    return steps+1
                
                if (cur-per,steps+1) not in visited and cur-per>0:
                    queue.append((cur-per,steps+1))
                    visited.add((cur-per,steps+1))
        
                
            
            