# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        
        node=root
        def dfs(node,great):
            
            if not node:
                return great 
            
            right=dfs(node.right,great)
            node.val+=right
            
            left=dfs(node.left,node.val)
            
            
            return left
        
        dfs(node,0)
        return root