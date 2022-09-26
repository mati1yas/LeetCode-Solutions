# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth=[0,0]
#                  depth,sum
        
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        
        
        def deepest(root,depth):
            
            if not root:
                return None
            
            if depth>self.depth[0]:
                self.depth=[depth,root.val]
            elif depth==self.depth[0]:
                self.depth[1]+=root.val
            
            deepest(root.left,depth+1)
            deepest(root.right,depth+1)
            
            
        
        deepest(root,0)
        return self.depth[1]