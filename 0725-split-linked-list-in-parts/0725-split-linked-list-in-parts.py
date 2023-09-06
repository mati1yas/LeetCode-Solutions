# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        
        
        partitions= [ ]
        
        
        slow=head
        fast = head
        
        total = 0
        while fast:
            
            total += 1
            fast = fast.next
            
      
        slow = head
        
        fast = head
        
        
        while k:
            
            if total%k ==0:
                curSize= (total//k)
            else:
                curSize= (total//k)+1
                
            temp= curSize   
            while fast and curSize!=1:
                
                curSize-=1
                
                fast= fast.next
                
            if fast:
                head= fast.next
                fast.next=None
                partitions.append(slow)
                slow=head
                fast=head
                
                
                k-=1
                total-=temp
            else:
                partitions.append(slow)
                k-=1
                total-=temp
            
                
            
            
        
        return partitions
                
            
            
        
            
            
            