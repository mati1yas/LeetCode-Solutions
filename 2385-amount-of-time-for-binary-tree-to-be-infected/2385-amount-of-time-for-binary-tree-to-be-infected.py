# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
      
    
        graph=defaultdict(list)
        
        
        def dfs(root,parent):
            
            if not root:
                return 
            
            if root and parent:
                graph[root.val].append(parent.val)
                graph[parent.val].append(root.val)
            
            dfs(root.left,root)
            dfs(root.right,root)
            
        dfs(root,None)
        
        queue= collections.deque()
        queue.append((start,0))
        dist=0
        
        visited=set()
        visited.add(start)
        while queue:
            cur,t=queue.popleft()
            dist=max(dist,t)
            for nbr in graph[cur]:
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append((nbr,t+1))
                
        return dist
                
            
            
        
        
            
            
            