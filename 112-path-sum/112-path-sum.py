# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(root,cursum):
            
            if not root:
                return None
            
            cursum-=root.val
            if root.left==None and root.right==None:
                
                return cursum==0
            
            return dfs(root.left,cursum) or dfs(root.right,cursum)
            
            
            
            
            
            
            
        
        return dfs(root,targetSum)
        
       

    
        
        
        
        
            