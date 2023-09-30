class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        
        
        

            
            
            
        mostBeautiful=0
        for i in range(len(maxHeights)):
            
            heights=[0 for _ in range(len(maxHeights))]
            
            heights[i] = maxHeights[i]
            
            
            # increasing side
            
            for j in range(i-1,-1,-1):
                
                
                heights[j]=min(maxHeights[j],heights[j+1])
            
            # decreasing side
            
            for j in range(i+1,len(maxHeights)):
                heights[j]=min(maxHeights[j],heights[j-1])
                
                
                
            mostBeautiful=max(sum(heights),mostBeautiful)
                
                
        return mostBeautiful 
                
                
                
                
            