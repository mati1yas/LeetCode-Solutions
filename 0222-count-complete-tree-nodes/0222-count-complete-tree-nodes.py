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
        
        def leftHeight(node):
            h=0
            while node:
                h+=1
                node=node.left
            return h
        def rightHeight(node):
            h=0
            while node:
                h+=1
                node=node.right
            return h
                
        
        
        
        # here am at specific node I have to calculate leftMost and rightMost height
        
        lh=leftHeight(root)
        
        rh=rightHeight(root)
        
        if lh==rh:
            return 2**lh-1
        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1
        