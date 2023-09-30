class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        
        
    
        stack = [ ]
        smallest= nums[0]
        
        for num in nums[1:]:
            
            while stack and stack[-1][0]<num:
                stack.pop()

            if stack and stack[-1][0]>num>stack[-1][1]:
                return True
            
            stack.append((num,smallest))
            smallest=min(smallest,num)
                 
        return False