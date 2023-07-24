# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        
        memo={}
        self.ans=0
        def goZigZag(root,goRight):
            
            
            
            if not root:
                return 0
            
            
            
            if (root,goRight) in memo:
                
                self.ans=max(self.ans,memo[(root,goRight)])
            else:
                left=goZigZag(root.left,True)
                right=goZigZag(root.right,False)
                memo[(root,goRight)]=(left,right)
                self.ans=max(self.ans,left,right)
                
            if goRight:                               
                return memo[(root,goRight)][1]+1
            else:                
                return memo[(root,goRight)][0]+1
            
            
            
            
            
        left=goZigZag(root.left,True)
        right=goZigZag(root.right,False)
        self.ans=max(self.ans,left,right)
        return self.ans
            