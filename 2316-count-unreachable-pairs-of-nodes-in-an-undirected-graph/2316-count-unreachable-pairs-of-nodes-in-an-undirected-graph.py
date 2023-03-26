class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        
        
        
        graph=defaultdict(list)
        
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
            
        
        
        
        connected=set()
        def bfs(start):
            queue=deque()
            queue.append(start)
            visited=set({start})
            connected.add(start)
            
            count=1
            
            while queue:
                
                cur=queue.popleft()
                
                for nbr in graph[cur]:
                    if nbr not in visited:
                        visited.add(nbr)
                        queue.append(nbr)
                        connected.add(nbr)
                        count+=1
            
            return count 
                
                
            
            
        total=0  
        for i in range(n):
            if i not in connected:
                r=bfs(i)
                
                total+=(n-r)*r
            
        return total//2
        