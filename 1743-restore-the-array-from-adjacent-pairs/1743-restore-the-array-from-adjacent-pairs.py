class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        
        adjacents=defaultdict(list)
        
        frequency=defaultdict(int)
        
        for start,end in adjacentPairs:
            adjacents[start].append(end)
            adjacents[end].append(start)
          
        startNode=None
        
        for node in adjacents:
            
            if len(adjacents[node])==1:
                startNode=node
                break
        
        
        self.ans=[startNode]
        self.visited=set({startNode})
        def dfs(node):           
            
            for nbr in adjacents[node]:
                if nbr not in self.visited:
                    self.visited.add(nbr)
                    self.ans.append(nbr)
                    dfs(nbr)
            
               
            
        dfs(startNode)
        return self.ans
                
        
        
                
                
        

        