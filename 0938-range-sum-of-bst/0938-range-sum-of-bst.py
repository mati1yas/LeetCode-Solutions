# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        
        
        def dfs(root):
            
            if not root:
                return 0
            
            
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            val=0
            if low<=root.val<=high:
                val=root.val
                
            return left+val+right
        
        return dfs(root)
                