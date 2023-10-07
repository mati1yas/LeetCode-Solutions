# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        
        
        
        
        
        self.column=defaultdict(list)
        queue=deque()
        queue.append((root,0,0))
        
        
        
        while queue:
            
            
            node,col,row = queue.popleft()
            
            if not node:
                continue
            
            self.column[col].append((row,node.val))
            
            
            
            queue.append((node.left,col-1,row+1))
            queue.append((node.right,col+1,row+1))
        
        
         
        ans=[]
        for col in sorted(self.column):
            ans.append([val for row,val in sorted(self.column[col])])
        
        return ans
        