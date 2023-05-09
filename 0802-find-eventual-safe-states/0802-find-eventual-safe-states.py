class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        digraph= defaultdict(list)
        
        
        for i,nbrs in enumerate(graph):
            
            digraph[i]= nbrs
            
            
            
        isSafe={}
        def dfs(node):
            
            
            
            if node in isSafe:
                return isSafe[node]
            
            
            isSafe[node]=False
            for nbr in digraph[node]:
                
                if not dfs(nbr):
                    return False
                
            isSafe[node]=True
            
            return True
        
    
        ans=[]
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
                
        return ans
                
        
        
                
                
                
            
                
            