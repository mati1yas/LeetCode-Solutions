# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def dfs(nums):
            if not nums:
                return 


            mid=len(nums)//2
            
            
            
            leftR=dfs(nums[:mid])
        
            rightR=dfs(nums[mid+1:])
            
            node=TreeNode(nums[mid])
            
            node.left=leftR
            node.right=rightR
            
            return node
            
            
            
            
            
            
            
            
            
            
            
        
        
        return dfs(nums)