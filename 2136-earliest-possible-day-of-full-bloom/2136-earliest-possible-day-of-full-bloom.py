class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        plants=[]
        
        for i in range(len(plantTime)):
            plants.append([plantTime[i],growTime[i]])
        
        plants.sort(key=lambda x: -x[1])
       
        
        lastPlantingTime=0
        bloomTime=0
        for timeToPlant,timeToGrow in plants:
            lastPlantingTime+=timeToPlant
            
            bloomTime=max(bloomTime,lastPlantingTime+timeToGrow)
        return bloomTime
            
            
            
            