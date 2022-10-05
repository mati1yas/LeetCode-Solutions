# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth==1:
            new=TreeNode(val)
            new.left=root
            
            return new
        
        
        def add(root,d):
            
            
            if not root:
                return None
            
            if depth==d:
                
                temp=root.left
                root.left=TreeNode(val)
                root.left.left=temp
                
                temp= root.right
                root.right=TreeNode(val)
                
                root.right.right=temp
                
                
            else:
                
                add(root.left,d+1)

                add(root.right,d+1)
            
        add(root,2)
        return root
        
            
            