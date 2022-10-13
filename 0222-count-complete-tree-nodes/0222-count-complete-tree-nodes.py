# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
        if not root:
            return 0
        
        def rightheight(node):
            d=0
            while node:
                d+=1
                node=node.right
            return d
            
        def leftheight(node):
            d=0
            while node:
                d+=1
                node=node.left
            return d
        
        lh=leftheight(root)
        rh=rightheight(root)
        
        if lh==rh:
            return 2**(rh)-1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
        
        
            
            
            
        
        
        
        
        
        
        