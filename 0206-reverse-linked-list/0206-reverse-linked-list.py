# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
    
        def reverse(root):
            
            
            if not root or not root.next:
                
                return root
             
            r=reverse(root.next)
            
            root.next.next=root
            root.next=None
            
            
            return r
            
        
        return reverse(head)
        
        