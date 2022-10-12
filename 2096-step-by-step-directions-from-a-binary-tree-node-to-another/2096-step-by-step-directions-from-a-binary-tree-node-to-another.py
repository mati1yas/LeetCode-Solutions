# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        self.start=None
        self.end=None
    
        def dfs(root,parent):
            
            if not root:
                return 
            
            root.parent=parent
            
            dfs(root.left,root)
            dfs(root.right,root)
            
            if root.val==startValue:
                self.start=root
            if root.val==destValue:
                self.end=root
            
            
            
        dfs(root,None)
        
        queue=collections.deque()
        visited=set()
        queue.append((self.start,""))
        visited.add(self.start.val)
        
        while queue:
            node,path=queue.popleft()
            
            if node==self.end:
                return path
            
            
            if node.parent and node.parent.val not in visited:
                queue.append((node.parent,path+"U"))
                visited.add(node.parent.val)
            
            if node.left and node.left.val not in visited:
                queue.append((node.left,path+"L"))
                visited.add(node.left.val)
            
            if node.right and node.right.val not in visited:
                queue.append((node.right,path+"R"))
                visited.add(node.right.val)
        
        
        