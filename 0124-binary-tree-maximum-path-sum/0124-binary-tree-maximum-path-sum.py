# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        def dfs(root):
            
            if not root:
                return [float("-inf"),float("-inf")]  # curPathMax,globalPathMax
            
            
            left=dfs(root.left)
            right=dfs(root.right)


            return [max(max(left[0],right[0])+root.val,root.val),max(left[1],left[0],right[0],right[1],left[0]+right[0]+root.val,root.val,max(left[0],right[0])+root.val)]
        
        
        return dfs(root)[1]
            
            
            
        