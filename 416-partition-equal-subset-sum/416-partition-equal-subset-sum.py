class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        
        s=set()
        s.add(0)
        
        for num in nums:
            
            ds=set()
            for elem in s:
                ds.add(elem+num)
                ds.add(elem)
            s=ds
        
        return True if sum(nums)//2 in s else False