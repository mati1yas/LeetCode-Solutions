class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        graph=defaultdict(list)
        visited=set()
        
        for start, end in connections:
            
            graph[start].append(end)
            graph[end].append(start)
            
        tirf=0
            
        def bfs(node):
            nonlocal tirf
            queue=deque()
            
            queue.append(node)
            
            edges=set()
            nodes=set()
            
            while queue:
                cur=queue.popleft()
                
                nodes.add(cur)
                
                
                for nbr in graph[cur]:
                    edges.add((cur,nbr))
                    
                    if nbr not in visited:
                        queue.append(nbr)
                        visited.add(nbr)
                        
            no_edges=len(edges)//2
            no_nodes=len(nodes)
            
            if no_edges:
            
                tirf+=no_edges-(no_nodes-1)
            
            
        
        disconnected=0
        for i in range(n):
            
            
            
            if i not in visited:
                
                disconnected+=1
                bfs(i)
                visited.add(i)
                
        
        return disconnected-1 if tirf+1>=disconnected else -1
                
            
            
        