# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        

        self.diff=0
        def dfs(node):

            if not node:
                return [float('inf'),float('inf')]


            left=dfs(node.left)
            right=dfs(node.right)

            if left[0]!=float('inf'):
                self.diff=max(self.diff,abs(left[0]-node.val),abs(left[1]-node.val))
            if right[0]!=float('inf'):
                self.diff=max(self.diff,abs(right[0]-node.val),abs(right[1]-node.val))

            mini=min(left[0],left[1],node.val,right[0],right[1])
            if left[0]==float('inf') and right[0]!=float('inf'):
                maxi=max(node.val,right[0],right[1])
            elif right[0]==float('inf') and left[0]!=float('inf') : 
                maxi=max(left[0],left[1],node.val)
            elif left[0]==float('inf') and right[0]==float('inf'):
                maxi=node.val
            else:
                maxi=max(left[0],left[1],node.val,right[0],right[1])
            
            return [mini,maxi]

        dfs(root)
        return self.diff