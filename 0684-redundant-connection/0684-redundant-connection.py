class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        def isConnected(start,end):
            
            if start==end:
                return True
            visited.add(start)
            for nbr in graph[start]:
                if nbr not in visited:
                    if isConnected(nbr,end):
                        return True
                    
            
        
        
        graph=defaultdict(list)
        
        for start,end in edges:
            visited=set()
            if start in graph and end in graph and isConnected(start,end):
                return [start,end]
            
            graph[start].append(end)
            graph[end].append(start)
        
        
        
        