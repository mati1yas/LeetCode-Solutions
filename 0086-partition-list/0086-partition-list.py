# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        
        smaller=ListNode()
        smaller_dummy=smaller
        greater=ListNode()
        greater_dummy=greater
        
        root=head
        found = False
        while root:
            
            if root.val>=x:
                greater.next=root
                greater=greater.next
                
            
            else:
                smaller.next=root
                smaller=smaller.next
            root=root.next
            
        greater.next=None
        smaller.next=greater_dummy.next
        return smaller_dummy.next
            
            
            