class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        pre=[nums[0]]
        
        for i in range(1,len(nums)):
            pre.append(nums[i]+pre[-1])
        
        return pre