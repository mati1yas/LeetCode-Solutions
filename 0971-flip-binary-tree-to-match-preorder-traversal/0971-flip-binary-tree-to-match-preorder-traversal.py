# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        
        if root.val!=voyage[0]:
            return [-1]
        
        self.pointer=0
        
        self.flipped=[]
        def dfs(root):
            if not root:
                return 
            if root.val!=voyage[self.pointer]:
                self.flipped=[-1]
            
                return 
            self.pointer+=1
            if root.left and self.pointer<len(voyage) and root.left.val!=voyage[self.pointer]:
                    self.flipped.append(root.val)
                    
                    dfs(root.right)
                    dfs(root.left)
                    
            else:
                
                dfs(root.left)
                dfs(root.right)
            
        dfs(root)
        if self.flipped and self.flipped[0]==-1:
            self.flipped=[-1]
        return self.flipped
        