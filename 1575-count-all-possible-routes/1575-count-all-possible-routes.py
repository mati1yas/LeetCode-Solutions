class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        
        
        self.memo={}
        mod=pow(10,9)+7
        def dfs(city,fuel):
            
            if fuel == 0:
                
                if city == finish:
                    return 1
                else:
                    return 0
            
            if (city ,fuel) in self.memo:
                
                return self.memo[(city,fuel)]
            
            total=0
            
            for i in range(len(locations)):
                
                if i == city :
                    continue
                    
                leftFuel=fuel-abs(locations[city]-locations[i])
                if leftFuel>=0 :
                    
                    total+=dfs(i,leftFuel)%mod
                    
            if city==finish:
                total+=1
            
            self.memo[(city,fuel)]=total%mod
            return total
        
        return dfs(start,fuel)%mod
                    
                
                    