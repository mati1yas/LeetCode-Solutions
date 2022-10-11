# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        def dfs(root,parent):
            if not root:
                return  
            if not root.left and not root.right:
                return chr(root.val+97)
            
            
            left=dfs(root.left,chr(root.val+97))
            right=dfs(root.right,chr(root.val+97))
            
            if not left or not right:
                return (left or right)+chr(root.val+97)
            
            if left+chr(root.val+97)+parent<right+chr(root.val+97)+parent:
                return left+chr(root.val+97)
            else:
                return right+chr(root.val+97)
            
        
            
            
            
        
        return dfs(root,chr(root.val+97))
        