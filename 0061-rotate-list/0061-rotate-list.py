# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if k==0 or not head:
            return head
        
        self.head=head
        self.rotate=None
        self.updated=False
        
        def recurse(root,l):
            
            
            if not root:
                self.rotate=k%l
                return 0
            
            
            r=recurse(root.next,l+1)
            
            if self.rotate:
                
                root.next=self.head
                self.head=root
                self.rotate-=1
            elif not self.rotate and not self.updated:
                root.next=None
                self.updated=True
            
            
        recurse(head,0)
        
        return self.head
            
            