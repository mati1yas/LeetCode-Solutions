class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj=defaultdict(list)
        
        for idx,(start,end) in enumerate(equations):
            
            adj[start].append((end,values[idx]))
            adj[end].append((start,1/values[idx]))
        
        
        
        def bfs(start,end):
            
            queue=collections.deque()
            queue.append((start,1,1))
            visited=set()
            if end not in adj:
                return float(-1)
            
            while queue:
                cur,parent,val=queue.popleft()
                
                if cur==end:
                    return val
                
                for nbr, dist in adj[cur]:
                    if nbr not in visited and nbr!=parent:
                        visited.add(nbr)
                        queue.append((nbr,cur,val*dist))
            return float(-1)
            
            
            
            
            
            
            
            
        ans=[]
        for start,end in queries:
            ans.append(bfs(start,end))
        
        return ans
            