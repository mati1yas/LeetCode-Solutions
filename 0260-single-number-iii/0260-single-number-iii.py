class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        
        freq=Counter(nums)
        
        return [num for num in freq if freq[num]==1]