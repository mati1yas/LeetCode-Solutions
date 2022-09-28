class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # height=[1,8,6,2,5,4,8,3,7]
        #         0,1,2,3,4,5,6,7,8
        #           |              |
        
        mx=0
        left=0
        right=len(height)-1
        while left<right:
            
            A=min(height[left],height[right])* (right-left)
            mx=max(mx,A)
            
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return mx
        