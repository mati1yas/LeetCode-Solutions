class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        
        graph = defaultdict(list)
        
        
        for a,b in edges:
            graph[a].append(b)
            
            graph[b].append(a)
            
        print(graph)    
        for center, nbrs in graph.items():
            
            if len(nbrs)>=2:
                return center