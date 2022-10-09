class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        
        self.result=[]
        
        def sub(index,arr):
            
            if index>=len(nums):
                self.result.append(arr)
                return
            
            sub(index+1,arr+[nums[index]])
            sub(index+1,arr)
            
        sub(0,[])
        return self.result