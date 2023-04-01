class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
        
        
        stack=[]
        leftSmall=nums[0]
        for num in nums[1:]:
            
            
          
            while stack and stack[-1][0]<=num:
                val,left=stack.pop()
            
                
            if stack and stack[-1][1]<num<stack[-1][0]:
                return True
                
                
            stack.append((num,leftSmall))
            leftSmall=min(num,leftSmall)
                
            
        return False
                
            
            
                
                