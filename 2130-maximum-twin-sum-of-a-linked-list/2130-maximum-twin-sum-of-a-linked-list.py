# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        
        values=[]
        
        node=head
        while node:
            values.append(node.val)
            node=node.next
            
        
        left=0
        right=len(values)-1
        
        
        maxTwinSum=0
        while left<right:
            
            maxTwinSum=max(maxTwinSum,values[left]+values[right])
            left+=1
            right-=1
        return maxTwinSum