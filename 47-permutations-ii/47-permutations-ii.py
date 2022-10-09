class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    
        self.r=[]
        self.result=[]
        def permutate(nums):
            
            
            if len(nums)==0:
                arr=self.result.copy()
                self.r.append(arr)
                return 
            recent=float('inf')
            for i in range(len(nums)):
                
                
                if nums[0]==recent:
                    n=nums.pop(0)
                    nums.append(n)
                    continue
                n=nums.pop(0)
                
                self.result.append(n)
                
                permutate(nums)
                self.result.pop()
                nums.append(n)
                recent=n
         
        nums.sort()
        permutate(nums)
        return self.r
                
                