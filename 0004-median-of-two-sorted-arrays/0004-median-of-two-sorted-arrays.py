class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        arr=nums1+nums2
        
        arr.sort()
        mid=(len(arr)//2)
        if len(arr)%2==0:
            
            
            return (arr[mid]+arr[mid-1])/2
        else:
            return arr[mid]
        
        