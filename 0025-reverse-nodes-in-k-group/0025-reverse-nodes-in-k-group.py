# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        def reverse(head,k):
            
            
            newHead,ptr=None,head
            
            while k:
                
                
                
                nextNode = ptr.next
                
                ptr.next=newHead
                
                newHead = ptr
                
                ptr= nextNode
                k-=1
            return newHead
    
       
        
        count=0
        ptr=head
        while count<k and ptr:
            count+=1
            ptr = ptr.next
            
        
        if count==k:
            
            
            reversedHead=reverse(head,k)
            
            head.next=self.reverseKGroup(ptr,k)
            
            
            return reversedHead
            
            
        return head
            
                