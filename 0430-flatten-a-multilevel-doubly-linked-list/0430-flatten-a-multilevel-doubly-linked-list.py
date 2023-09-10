"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return head

        temp_head=Node(None,None,head,None)

        def dfs(prev,cur):
            if not cur:
                return prev

            # creating the link between the current and the previous 
            prev.next = cur
            cur.prev = prev
            
            temp = cur.next
            parent = dfs(cur,cur.child)    # forms flattened linked list before going to the next fo the current node


            cur.child=None  # this detaches the child 

            merged=dfs(parent,temp)
            return merged
    
        dfs(temp_head,head)

        temp_head.next.prev=None
        return temp_head.next


