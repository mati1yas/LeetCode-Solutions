# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        
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
        
        ans=[]
        
        def bfs(start):
           
            queue=collections.deque()
            
            queue.append((start,0))
            visited=set({start})
            
            while queue:
                
                cur,dist=queue.popleft()
                
                if dist==k:
                    ans.append(cur)
                
                for nbr in graph[cur]:
                    if nbr not in visited:
                        
                        queue.append((nbr,dist+1))
                        visited.add(nbr)
               
        bfs(target.val)
        
        return ans
        
        
            
            
            
            
            
            
            
            