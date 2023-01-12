class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        
        graph=defaultdict(list)
        
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
#          will build new array from all return 
#          increment the value of the ord of current node
#          update answer array with current sum of array which is going to be returned
        
        self.answer=[0 for _ in range(n)]
        def dfs(node,visited):
            
            
            counts=[0 for i in range(26)]
            for nbr in graph[node]:
                
                if nbr not in visited:
                    visited.add(nbr)
                    ret=dfs(nbr,visited)
                    
                    for i in range(len(ret)):
                        counts[i]+=ret[i]
                        
            indexOfCurrentNode=ord(labels[node])-97
            counts[indexOfCurrentNode]+=1
            
            self.answer[node]=counts[indexOfCurrentNode]
            
            
            
            
            return counts
        dfs(0,{0})
        
        return self.answer
                    
                