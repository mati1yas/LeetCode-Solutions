# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        m,n=left,right
        left,right=head,head
        stop=False
        def reverse(right,m,n):
            nonlocal left,stop
            if n==1:
                return 
            
            
            if m>1:
                left=left.next
                
            right=right.next
            
            reverse(right,m-1,n-1)
            
            if left==right or right.next==left:
                stop=True
                
            if not stop:
                left.val,right.val=right.val,left.val
            
                left=left.next
        reverse(right,m,n)
        
        return head
        
        