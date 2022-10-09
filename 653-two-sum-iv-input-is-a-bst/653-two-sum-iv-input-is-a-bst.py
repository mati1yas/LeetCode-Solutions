# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        self.set=set()
        
        self.found=False
        def dfs(root):
            
            if not root:
                return 
            
            dfs(root.left)            
            
            
            if k-root.val in self.set:
                self.found=True
            self.set.add(root.val)
            dfs(root.right)
        
        dfs(root)
        return self.found