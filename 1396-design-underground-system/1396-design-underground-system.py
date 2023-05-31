class UndergroundSystem:

    def __init__(self):
        self.checkInTimes={}
        
        self.travels=defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.checkInTimes[id]=(stationName,t)
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        if id in self.checkInTimes:
            endStation=stationName
            endTime = t
            startStation,entryTime=  self.checkInTimes[id]
            self.travels[(startStation,stationName)].append(endTime-entryTime)
            
            
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        totalTravelsTime = sum(self.travels[(startStation,endStation)])
        numberOfTravels= len(self.travels[(startStation,endStation)])
        
        return totalTravelsTime/numberOfTravels
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)