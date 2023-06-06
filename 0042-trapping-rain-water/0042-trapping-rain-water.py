class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        stack =[]
        ans=0
        
        
        for idx , h in enumerate(height):
            
            
            while stack and height[stack[-1]] < h:
                
                i= stack.pop()
                
                if not stack :
                    break
                    
                
                width = idx-stack[-1]-1
                
                
                trapped= min(height[stack[-1]] , height[idx]) - height[i]
                ans+= (width * trapped )
                
            stack.append(idx)
                
        return ans