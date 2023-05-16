# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        if not head or not head.next:
            return head
        simple=ListNode()
        simple.next=head
        
        start=simple
        
        
        
        middle = simple.next
        
        
        last=simple.next.next
        
       
        while last:
            

            
            middle.next=last.next
            last.next=start.next
            start.next=last



            start=middle
            middle=middle.next
            last=middle.next if middle else None           
        return simple.next
            
            
        
        
        
        