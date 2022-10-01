class Solution:
    
    def __init__(self):
        self.maxrobbed=0
        self.arr=[]
        self.memo={}
    def robber(self,i):
            
            if i>=len(self.arr):
                return 0
            
            robbed=0
            
            for x in range(i+2,len(self.arr)):               
                
                if x not  in self.memo:
                    
                    r=self.robber(x)
                else:
                    r=self.memo[x]
                robbed=max(r,robbed)
               
            self.memo[i]=robbed+self.arr[i]
            
            return self.memo[i]
            
    
    def helper(self,arr):
        
        self.maxrobbed=0
        self.memo={}
        self.arr=arr
        
           
        for i in range(len(arr)):
            
            if i in self.memo:
                self.maxrobbed=max(self.maxrobbed,self.memo[i])
                continue

            self.maxrobbed=max(self.maxrobbed,self.robber(i))
        return self.maxrobbed
                
        
    
    
    
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
        
        
        
        
        
        
          
        
        
        
        