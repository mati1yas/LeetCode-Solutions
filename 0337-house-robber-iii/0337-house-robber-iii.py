# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo={}
        
        def dfs(root,decision):
            
            if not root:
                return 0
            
            
            takeL=0
            takeR=0
            
            notTakeL=0
            notTakeR=0
            
            if (root, decision) in memo:
                
                return memo[(root,decision)]
            
            if not decision:
                
                takeL=dfs(root.left,True)
                takeR=dfs(root.right,True)
            notTakeL=dfs(root.left,False)
            notTakeR=dfs(root.right,False)
            
            
            if not decision:
                memo[(root,decision)]=max(root.val+takeL+takeR,notTakeL+notTakeR)
                return max(root.val+takeL+takeR,notTakeL+notTakeR)
            
            memo[(root,decision)]=notTakeL+notTakeR
            return notTakeL+notTakeR
            
                
            
            
        
        
        
        return dfs(root,False)