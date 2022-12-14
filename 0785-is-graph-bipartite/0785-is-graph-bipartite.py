class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        
        relation=defaultdict(list)
        
        for i,nbrs in enumerate(graph):
            for nbr in nbrs:
                relation[nbr].append(i)
            relation[i].extend(nbrs)
            
        
        visited=set()
        def bfs(node):
            blue=set()
            red=set()
            queue=collections.deque()
            queue.append((node))
            blue.add(node)
            
            while queue:
                cur=queue.popleft()
                visited.add(cur)
                bl=True
                if cur not in blue:
                    bl=False


                for nbr in graph[cur]:
                    
                    if nbr not in visited:
                        queue.append(nbr)
                    if bl:
                        if nbr in blue:
                            return False
                        red.add(nbr)
                    else:
                        if nbr in red:
                            return False
                        blue.add(nbr)
            return True

        for i in range(len(graph)):
            
            if i in visited:
                continue
            if not bfs(i):
                return False
        
        
        return True



