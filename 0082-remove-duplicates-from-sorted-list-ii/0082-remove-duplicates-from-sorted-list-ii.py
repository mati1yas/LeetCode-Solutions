# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        #      |
        # None 1,2,3,3,4,4,5
        # |      |      
        
        if not head or not head.next:
            return head
        
        
        
        dummy=ListNode()
        
        dist=dummy
        slow=head
        dist.next= slow
        fast=head.next
        
        
        
        
        while fast :
            
            
            
            skipped=False
            while fast and fast.val == slow.val:
                skipped = True
                fast=fast.next
            
            
            if skipped:
                dist.next=fast
                
                if fast:
                    slow.next=fast.next
                    slow=fast
                    fast=fast.next

                else:
                    break
            else:
                
                dist=slow
                dist.next=fast
                slow=fast
                slow.next =fast.next
                fast=fast.next

           
            
        
        return dummy.next
            
            