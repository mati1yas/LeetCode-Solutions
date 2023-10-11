# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        
        
        
        rem=0
        
        res=n=ListNode(0)
        
        while l1 or l2 or rem:
            
            tot=rem
            if l1:
                tot+=l1.val
                l1=l1.next
            
            if l2:
                tot+=l2.val
                l2=l2.next
            
            
            
            rem,val = divmod(tot,10)
            
            n.next=ListNode(val)
            n=n.next
        return res.next