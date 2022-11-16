class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        jar=capacity
        steps=0
        for idx,plant in enumerate(plants):
            
           
            if jar<plant:
                jar=capacity-plant
                
                steps+=2*idx+1
            else:
                jar-=plant
                steps+=1
        return steps
            
            