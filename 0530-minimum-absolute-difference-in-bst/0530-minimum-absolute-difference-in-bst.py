# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        
        
        nodes = [ ]
        
        
        def dfs(root):
            
            
            if not root:
                return False
            
            
            nodes.append(root.val)
            
            dfs(root.left)
            dfs(root.right)
            
            
        dfs(root)
        
        
        minDiff= float('inf')
        nodes.sort()
        for idx in range(1,len(nodes)):
            val1= nodes[idx]
            val2= nodes[idx-1]
            minDiff= min(minDiff, abs(val1-val2))
                    
        return minDiff
                    
            
        