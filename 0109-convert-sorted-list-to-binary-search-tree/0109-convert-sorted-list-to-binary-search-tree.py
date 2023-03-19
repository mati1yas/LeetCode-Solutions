# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        root=head
        arr=[]
        while root:
            arr.append(root.val)
            
            root=root.next
        
        
        def dfs(left,right):
            
            if left>right:
                return 
            
            mid=(left+right)//2
            
            node=TreeNode(arr[mid])
            node.left=dfs(left,mid-1)
            node.right=dfs(mid+1,right)
            
            
            return node
            
            
        
        return dfs(0,len(arr)-1)
            
            
            