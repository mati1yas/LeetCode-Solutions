class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph=defaultdict(list)

        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)        

        visited=set()

        def dfs(node,visited):
          
            total=0
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    total+=dfs(nbr,visited)
            
            if hasApple[node]:
                total+=2
            elif total!=0:
                total+=2
            
            return total
        ret= dfs(0,{0}) 
        return ret-2 if ret>0 else ret

         
            
