# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        
        graph=defaultdict(list)
        
        def binaryDfs(root):
            
            if not root:
                return 
            
            
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                            
            
            if root.right:
                
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                
                
            binaryDfs(root.left)
            binaryDfs(root.right)
            
            
        binaryDfs(root)
        
        
        queue=collections.deque()
        queue.append((start,0))
        
        visited=set({start})
        ans=0  
        while queue:
            cur,dist=queue.popleft()
            ans=max(ans,dist)
            
            for nbr in graph[cur]:
                if nbr not in visited:
                    queue.append((nbr,dist+1))
                    visited.add(nbr)
                    
        return ans
            