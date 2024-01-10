# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        leafs=[]
        
        def dfs(root):
            
            if not root:
                return 
            
            if not root.left and not root.right:
                
                leafs.append(root.val)
                
                
            dfs(root.left)
            dfs(root.right)
         
        dfs(root1)
        seq1=leafs
        leafs=[]
        dfs(root2)
        seq2=leafs
        return seq1==seq2
        
        