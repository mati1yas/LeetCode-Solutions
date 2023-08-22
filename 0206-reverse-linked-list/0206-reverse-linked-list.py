# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
    
        dummy=None
        slow=dummy
        cur=head
        while head:
            
            temp=head.next
            head.next=slow
            slow=head
            head=temp
            
        return  slow
            
            
        
        
        
        