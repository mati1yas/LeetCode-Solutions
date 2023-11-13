class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        
        
        

            
        mostBeautiful= 0 
    
        for i in range(len(maxHeights)):
            
            
            heights = [ maxHeights[i] for i in range(len(maxHeights))]
            
            
            
            for j in range(i-1,-1,-1):
                
                heights[j]=min(heights[j],heights[j+1])
                
                
            for j in range(i+1,len(maxHeights)):
                
                heights[j]=min(heights[j],heights[j-1])
             
            mostBeautiful= max(mostBeautiful,sum(heights))
            
            
        return mostBeautiful
                
            
                
                
            