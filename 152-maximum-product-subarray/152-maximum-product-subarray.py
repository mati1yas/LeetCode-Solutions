class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res=max(nums)
        
        curmin,curmax=1,1
        
        for num in nums:
            
            if num==0:
                curmin=1
                curmax=1
            tempmax=curmax
            curmax=max(curmin*num,curmax*num,num)
            curmin=min(curmin*num,tempmax*num,num)
            res=max(res,curmax,curmin)
        return res