# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        
        
        def dfs(root,maxParent):
            
            if not root:
                return 0
            
            
            maxParent=max(root.val,maxParent)
            left=dfs(root.left,maxParent)
            right=dfs(root.right,maxParent)
            
            
            add=0
            
            if maxParent<=root.val:
                add+=1
                
            return left+right+add
        
        return dfs(root,float('-inf'))