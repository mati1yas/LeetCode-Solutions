import heapq as h
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        h.heapify(nums)
        
        
        sorted_array=[]
        
        while nums:
            sorted_array.append(h.heappop(nums))
        return sorted_array