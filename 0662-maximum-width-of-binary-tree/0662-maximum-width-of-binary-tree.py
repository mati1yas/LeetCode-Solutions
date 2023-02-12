# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        self.level=defaultdict(list)
        def dfs(node,row,col):
            
            
            if not node:
                return 
            self.level[row].append(col)
            
            
            dfs(node.left,row+1,2*col+1)
            dfs(node.right,row+1,2*col+2)
            
            
            
        dfs(root,0,0)
            
       
        
        width=0
        
        for level in self.level.values():
            
            width=max(width,max(level)-min(level))
        return width+1
            
            