# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(current,prev):
            
            if not current:
                return prev
            
            left,right=current.left,current.right
            
            if prev:
                prev.right=current
            current.left=None
            
            
            left_prev=dfs(left,current)
            right_prev=dfs(right,left_prev)
            
            
            
            
            
            return right_prev
            
            
        dfs(root,None)
        
        
        
        
        
        
        