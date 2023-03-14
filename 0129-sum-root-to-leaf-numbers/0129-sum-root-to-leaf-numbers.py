# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
    
        def dfs(root,number):
            
            if not root:
                return 0
            
            number=number*10+ root.val
            
            if not root.left and not root.right:
                return number
            left=dfs(root.left,number)
            right= dfs(root.right,number)
            
            return left+right
            
            
        return dfs(root,0)
        