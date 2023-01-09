"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        queue=collections.deque()
        
        if not root:
            return []
        queue.append(root)
        levelOrder=[]
        while queue:
            level=[]
            for i in range(len(queue)):
                cur=queue.popleft()
                if cur:
                    level.append(cur.val)
                    for child in cur.children:
                        queue.append(child)
            
            levelOrder.append(level)
        
        return levelOrder

