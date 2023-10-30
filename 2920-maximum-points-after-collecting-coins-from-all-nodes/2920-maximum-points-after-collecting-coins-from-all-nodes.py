class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        
        
        graph= defaultdict(list)
        
        
        for a,b in edges:
            
            graph[a].append(b)
            graph[b].append(a)
            
            
            
        visited=set()  
        
        self.memo={}
        
        def dfs(node,factor,par):
            
            if pow(0.5,14)>=factor:
                return 0
            
            if (node,factor) in self.memo:
                return self.memo[(node,factor)]
            
#             first way robing 
          
    
           

            tot1=(factor*coins[node])-k
            for nbr in graph[node]:
                if nbr != par:
                    tot1+=dfs(nbr,factor,node)
                
                
            tot2= (factor*coins[node])//2
            
            
            for nbr in graph[node]:
                
                 if nbr != par:
                
                    tot2+=dfs(nbr,factor*0.5,node)
                
            self.memo[(node,factor)] = max(tot1,tot2)
            return max(tot1,tot2)
        
        return int(dfs(0,1,-1))
        