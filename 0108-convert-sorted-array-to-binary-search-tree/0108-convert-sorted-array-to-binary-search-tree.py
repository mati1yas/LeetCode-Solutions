# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def dfs(left , right):
            
            
            if left>right:
                
                return 
            
            mid=(left+right)//2
            
            leftR=dfs(left,mid-1)
        
            rightR=dfs(mid+1,right)

            node=TreeNode(nums[mid])
            
            node.left=leftR
            node.right=rightR
            
            return node
            
        
        return dfs(0,len(nums)-1)