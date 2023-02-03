# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        self.column=defaultdict(list)
        
        
        def dfs(node,col,row):
            
            if not node:
                return 
            
            self.column[col].append((row,node.val))
            
            dfs(node.left,col-1,row+1)
            dfs(node.right,col+1,row+1)
            
        dfs(root,0,0)
        
        
        ans=[]
        for col in sorted(self.column):            
            ans.append([y for x,y in sorted(self.column[col]) ])
        
        return ans
        