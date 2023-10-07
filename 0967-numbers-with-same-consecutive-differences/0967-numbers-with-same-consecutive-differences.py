class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        
        queue=deque()
        
        
        for i in range(1,10):
            
            queue.append(i)
            
        
        ans=[]
        
        visited=set()
        while queue:
            
            cur=queue.popleft()
            
            
            if cur>=pow(10,n-1):
                ans.append(cur)
                
                continue
                
            
                
            
            last=str(cur)[-1]
            
            if int(last)-k>=0:
                new=cur*10+(int(last)-k)
                
                if new not in visited:
                    visited.add(new)
                    queue.append(new)
                
            if int(last)+k<=9:
                new=cur*10+(int(last)+k)
                if new not in visited:
                    visited.add(new)
                    queue.append(new)
              
        return ans
            
            
            