# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root1,root2):
            
            
            if not root1 and not root2:
                return True
            
            if not root1:
                return False
            
            if not root2:
                return False
            
            if root2.val!=root1.val:
                return False
            
            left=dfs(root1.left,root2.right)
            right=dfs(root1.right,root2.left)
            
            return left and right
        
        return dfs(root,root)