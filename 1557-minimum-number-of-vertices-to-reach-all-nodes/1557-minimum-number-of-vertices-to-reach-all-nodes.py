class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        
        indegrees = defaultdict(int)
        
        
        for start , end in edges:
            
            indegrees[end]+=1
            
        
        ans =[ ]
        
        for node in range(n):
            
            
            if indegrees[node] == 0:
                ans.append(node)
                
                
        return ans