# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        self.level=defaultdict(list)
        
        
        def dfs(root,row,col):
            
            if not root:
                return 
            
            
            self.level[row].append(col)
            
            
            dfs(root.left,row+1,2*col+1)
            dfs(root.right,row+1,2*col+2)
            
            
        dfs(root,0,0)
        
    
        width=float('-inf')
        for cols in self.level.values():
            
            width=max(width,max(cols)-min(cols))
            
            
        return width +1
            