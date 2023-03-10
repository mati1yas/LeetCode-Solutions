# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        
        self.root=head
        
        self.elements=[]
     
        
        cur=head
        
        while cur:
            self.elements.append(cur.val)
            cur = cur.next
            
        
    def getRandom(self) -> int:       
       
        return random.choice(self.elements)
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()