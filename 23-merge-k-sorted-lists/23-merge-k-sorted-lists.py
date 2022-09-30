# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        self.nodes=[]
        head=point=ListNode()
        
        for nodes in lists:
            while nodes:
                self.nodes.append(nodes.val)
            
                nodes=nodes.next
        
        for x in sorted(self.nodes):
            
            point.next=ListNode(x)
            point=point.next
        return head.next
            
            
            
            