class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        jumps=[float('inf')]*len(nums)
        jumps[-1]=0
        
        totalJumps=0
        for i in range(len(nums)-1,-1,-1):
            
            minJumps=float('inf')
            for j in range(i,min(i+nums[i]+1,len(nums))):
    
                minJumps=min(jumps[j],minJumps)
            if i==len(nums)-1:
                jumps[i]=0
                continue
            jumps[i]=minJumps+1
        return jumps[0]
                
                
                
                
                