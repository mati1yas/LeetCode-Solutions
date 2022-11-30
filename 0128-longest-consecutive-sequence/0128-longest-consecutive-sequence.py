class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        nums.sort()
        
        left=0
        right=1
        
        long=0
        count=1
        print(nums)
        while right<len(nums):
            
            if nums[right]!=nums[left]:
                if abs(nums[left]-nums[right])==1:
                    count+=1
                else:
                    long=max(long,count)
                    count=1
            right+=1
            left+=1
        long=max(long,count)
        return long