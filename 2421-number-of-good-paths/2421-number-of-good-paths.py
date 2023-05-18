class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        
        
        
        
        
        graph = defaultdict(list)
        
        
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        
        
        sameValueNodes= defaultdict(list)
        
        for i,val in enumerate(vals):
            
            sameValueNodes[val].append(i)
            
        self.parent={i:i for i in range(len(vals))}
        def find(node):
            
            if node != self.parent[node]:
                self.parent[node]=find(self.parent[node])
                
            return self.parent[node]
            
            
        def union(node1,node2):
            
            p1 = find(node1)
            p2 = find(node2)
            
            if p1<p2:
                self.parent[p2]=p1
            else:
                self.parent[p1]=p2
                
                
        goodPath=0
        for k in sorted(sameValueNodes):
            
            for node in sameValueNodes[k]:
                
                for nbr in graph[node]:
                    if vals[node]>=vals[nbr]:
                        union(node,nbr)
            
            
            count=defaultdict(int)
            
            for node in sameValueNodes[k]:
                par=find(node)
                count[par]+=1
                
            for c in count:
                
                goodPath+=(count[c]*(count[c]+1))//2
                
        return goodPath






            
        
            