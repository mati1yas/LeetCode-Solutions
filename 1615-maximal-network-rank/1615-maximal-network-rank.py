class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        
        graph=defaultdict(set)
        
        edge_count=defaultdict(int)
        
        for a,b in roads:
            
            graph[a].add(b)
            graph[b].add(a)
            edge_count[a]+=1
            edge_count[b]+=1
            
        rank=float('-inf')
        
        for node1 in range(n):
            for node2 in range(node1,n):
                
                if node1==node2:
                    continue
                
                if node1 in graph[node2]:
                    rank=max(rank,edge_count[node1]+edge_count[node2]-1)
                    
                else:
                    rank=max(rank,edge_count[node1]+edge_count[node2])

                    
        return rank 