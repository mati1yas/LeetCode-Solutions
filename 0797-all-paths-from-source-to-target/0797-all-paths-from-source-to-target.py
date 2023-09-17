class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        digraph={}
        
        
        for idx, nbrs in enumerate(graph):
            
            digraph[idx]=nbrs
            
        ans=[]
        n=len(graph)
        def dfs(node,path):           
            
            if node == n-1:
                ans.append(path+[node])
                return 
            
            
            for nbr in digraph[node]:
                dfs(nbr,path+[node])
                
        
        dfs(0,[])
            
        return ans
            