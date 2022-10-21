import heapq as h
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        
        distance=[(abs(x-val),val) for val in arr]
        
       
        h.heapify(distance)
        ans=[]
        while  len(ans)<k:
            
            popped=h.heappop(distance)
            ans.append(popped[1])
        
        ans.sort()
        return ans
        
        
        
        
        
        
        
        
        
        
#         left=0
#         right=len(arr)-k
#         # we will have four boundaries 
#         #  left   arr[mid]    arr[mid+k]    right
#         while left<right:
#             mid=(left+right)//2
            
            
#             if x<=arr[mid]:
#                 right=mid
#             elif x>= arr[mid+k]:
#                 left=mid+1
# #             the other case is when in between  the two middle boundaries
            
#             elif x-arr[mid]>arr[mid+k]-x:
#                 left=mid+1
#             else:
#                 right=mid
        
#         return arr[left:left+k]
        
        
            
            