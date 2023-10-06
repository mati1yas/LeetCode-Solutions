class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        leftMaximum , rightMaximum = [0]*len(height), [0]*len(height)
        
        
        
        for i in range(1,len(height)):
            
            leftMaximum[i] = max(leftMaximum[i-1],height[i-1])
            
        for i in range(len(height)-2,-1,-1):
            
            rightMaximum[i]=max(rightMaximum[i+1],height[i+1])
            
        ans=0
        for i in range(len(height)):
            
            waterLevel=min(leftMaximum[i],rightMaximum[i])
            
            if waterLevel>= height[i]:
                
                ans+=(waterLevel-height[i])
                
        return ans