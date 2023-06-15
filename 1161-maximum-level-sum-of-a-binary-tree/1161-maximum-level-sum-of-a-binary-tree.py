# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        
        
        queue= collections.deque()
        
        queue.append(root)
        
        ans = 0
        maxSum = float('-inf')
        level=0
        while queue:
            
            
            
            tot=0
            flag=False
            
            for i in range(len(queue)):
                
                node = queue.popleft()
                if node :
                    tot+=node.val
                    flag=True
                    
                    queue.append(node.left)
                    queue.append(node.right)
            
            
            if not flag:
                break
            if tot> maxSum:
                ans=level
                maxSum=tot
            
            level+=1
            
            
            
            
        return ans+1
                