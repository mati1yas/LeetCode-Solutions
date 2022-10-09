class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        
        self.result=[]
        def sub(index,arr):
            
            # if index>=len(nums):
                # if arr not in self.result:
            self.result.append(arr)
                
            recent =float('inf') 
            for i in range(index,len(nums)):
                
                if recent==nums[i]:
                    
                    continue
                sub(i+1,arr+[nums[i]])
                # sub(i+1,arr)
                recent=nums[i]
                
                
                
        nums.sort() 
        sub(0,[])
        return self.result