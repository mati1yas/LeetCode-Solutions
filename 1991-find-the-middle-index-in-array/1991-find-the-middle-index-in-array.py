class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return 0
        pre=[0]
        tot=sum(nums)
        for i in range(len(nums)):
            if pre[-1]==tot-(pre[-1]+nums[i]):
                return i
            pre.append(pre[-1]+nums[i])
       
        return -1
       