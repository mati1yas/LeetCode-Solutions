
import heapq as h
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        
        
        graph=defaultdict(list)
        
        for child ,par in enumerate( parent):
            graph[par].append(child) 
        
        self.maxPath=0      
        
        
        def dfs(node):
            
            childs=[]
            h.heapify(childs)
            
            for child in graph[node]:
                r=dfs(child)
                if r[1]!=s[node]:
                    h.heappush(childs,(-1*r[0],r[1]))
                    
            first=0         
            second=0
            
            if len(childs)>=1:
                first=(h.heappop(childs)[0])
                first*=-1
                
            if len(childs)>=1:
                second=(h.heappop(childs)[0])
                second*=-1
            self.maxPath=max(self.maxPath,first+second+1)           
            
            return (first+1,s[node])
        dfs(0)
        return self.maxPath
            
        