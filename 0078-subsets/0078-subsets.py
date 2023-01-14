class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.ret=[]
        
        def generateSubsets(subset,i):
            
            if i>=len(nums):
                
                return [subset]
            
            
            ret=[]
        
            take=generateSubsets(subset+[nums[i]],i+1)
            not_take=generateSubsets(subset,i+1)   
            
            ret.extend(take)
            ret.extend(not_take)
            
            return ret
            
            
            
        return generateSubsets([],0)
        