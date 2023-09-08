class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        print(costs)
        
        costs=sorted(costs, key= lambda x:x[1]-x[0])
        print(costs)
        
        half = len(costs)//2
        totalCosts=0
        for idx,(a,b) in enumerate(costs):
            
            if idx<half:
                totalCosts+=b
            else:
                totalCosts+=a
            
        return totalCosts
            