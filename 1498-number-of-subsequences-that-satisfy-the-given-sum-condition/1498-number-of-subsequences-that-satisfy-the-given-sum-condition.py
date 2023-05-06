class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        mod = 10 ** 9 + 7
        
        count=0
        for i in range(len(nums)):
            rightVal=target-nums[i]
            
            rightIndex=bisect_right(nums,rightVal)-1
              
            if rightIndex>=i:
            
                count+=pow(2,rightIndex-i,mod)
              
        return count %mod