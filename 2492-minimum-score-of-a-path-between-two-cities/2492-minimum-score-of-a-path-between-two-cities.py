class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in roads:
            graph[u][v] = graph[v][u] = w
        
        res = inf
        visited = set()
        myDeque = deque([1])

        while myDeque:
            node = myDeque.popleft()
            for adj, scr in graph[node].items():
                if adj not in visited:
                    myDeque.append(adj)
                    visited.add(adj)
                res = min(res,scr)
                
        return res