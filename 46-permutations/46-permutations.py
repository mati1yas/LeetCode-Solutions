class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        
        self.r=[]
        self.result=[]
        def permutate(nums):
            
            if len(nums)==0:
                arr=self.result.copy()
                self.r.append(arr)
                return 
            
            for i in range(len(nums)):
                n=nums.pop(0)   
                self.result.append(n) 
                
                permutate(nums)
                
                self.result.pop()
                
                nums.append(n)
                
            
            
        
        
        
        
        permutate(nums)
        return self.r