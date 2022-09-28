class NumArray:

    def __init__(self, nums: List[int]):
        
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        self.nums=nums
        

    def sumRange(self, left: int, right: int) -> int:
        
        answer=self.nums[right]
        
        leftSide=0
        if left-1>=0:
            leftSide=self.nums[left-1]
        
        return answer-leftSide
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)