# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        graph=defaultdict(int)
        
        self.ans=(float('-inf'),-1)
        def dfs(root,level):
            
            if not root:
                return 
            
            graph[level]+=root.val
                  
            dfs(root.left,level+1)
            dfs(root.right,level+1)            
            
        
        dfs(root,1)
       
        for level, tot in graph.items():
            if graph[level]>self.ans[0]:                
                self.ans=(graph[level],level)
            
            
        return self.ans[1]