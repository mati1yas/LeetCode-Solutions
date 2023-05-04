class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
       
        
        Rides=deque([i for i in range(len(senate)) if senate[i]=="R"]) 
        Dires=deque([i for i in range(len(senate)) if senate[i] == "D"])
        
        
        while Rides and Dires:
            
            r,d = Rides.popleft(),Dires.popleft()
            
            if d> r :
                Rides.append(len(senate)+r)
            
            else:
                Dires.append(len(senate)+d)
                
        return "Dire" if Dires else "Radiant"