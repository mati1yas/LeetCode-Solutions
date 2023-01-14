class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.ret=[]
        
        def generateSubsets(subset,i):
            
            if i>=len(nums):
                self.ret.append(subset)
                return subset
            
            
        
            take=generateSubsets(subset+[nums[i]],i+1)
            not_take=generateSubsets(subset,i+1)
            
            
            
            return [take]+[not_take]
        generateSubsets([],0)
        return self.ret