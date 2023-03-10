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
        self.count=0
        
        cur=head
        
        while cur:
            self.elements.append(cur.val)
            cur = cur.next
            self.count+=1
            
        
    def getRandom(self) -> int:       
       
        return random.choice(self.elements)
        index=random.randint(0,self.count)
        cur=self.root
        while cur.next and index:
            cur=cur.next
            index-=1
        
        return cur.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()