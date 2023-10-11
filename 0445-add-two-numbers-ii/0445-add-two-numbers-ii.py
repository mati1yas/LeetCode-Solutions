# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def reverse(head):
            
            last=None
            
            while head:
                tmp=head.next
                head.next=last
                
                last=head
                head=tmp
                
            return last
            
            
            
            
            
        l1=reverse(l1)
        l2=reverse(l2)
        carry=0
        
        head=None
        while l1 or l2:
            
            if l1:
                x1=l1.val
            else:
                x1=0
                
            if l2:
                x2=l2.val
            else:
                x2=0
                
            
           
            
            carry,val = divmod(carry+x1+x2,10)
            
            cur=ListNode(val)
            cur.next=head
            head=cur
            
            
            if l1:
                l1=l1.next
            else:
                l1=None
                
            if l2:
                l2=l2.next
            else:
                l2=None
                
                
                
        if carry:            
            cur=ListNode(carry)
            cur.next=head
            head=cur
                
        return head
            
            

