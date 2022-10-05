class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        
        s=set()
        s.add(0)
        target=sum(nums)//2
        
        for i in range(len(nums)-1,-1,-1):
            ds=set()
            for elem in s:
                ds.add(elem+nums[i])
                ds.add(elem)
                if target in s:
                    return True
            s=ds
        
        return True if target in s else False