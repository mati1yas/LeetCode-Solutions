class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        
        index={x:i for i,x in enumerate(nums)}
        
        
        for op in operations:
            nums[index[op[0]]]=op[1]
            index[op[1]]= index[op[0]]  
        return nums