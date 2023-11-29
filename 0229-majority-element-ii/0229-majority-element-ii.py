class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        
        
        freq=Counter(nums)
        n = len(nums)
        ans= [ ]
        for num in nums:
            if freq[num]>(n/3):
                ans.append(num)
                
                
        return list(set(ans))