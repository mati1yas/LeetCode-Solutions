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
            
            
            
            curMaxPath=max(left[0]+root.val,right[0]+root.val,root.val)
            
            globalMax=max(left[0]+root.val,right[0]+root.val,root.val,right[0],left[0],left[0]+right[0]+root.val,right[1],left[1])
            


            return [curMaxPath,globalMax]
        
        return dfs(root)[1]
            
            
            
        