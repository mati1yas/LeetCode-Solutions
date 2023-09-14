"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        queue=deque()
        queue.append(root)
        while queue:
            
            newLevel=[]
            for i in range(len(queue)):
                
                cur=queue.popleft()
                
                if cur:
                    cur.next=queue[0] if queue else None
                    if cur.left:
                        newLevel.append(cur.left)
                    if cur.right:
                        newLevel.append(cur.right)
                    
            queue=deque(newLevel)
        
        return root