class UndergroundSystem:

    def __init__(self):
        
        self.checkInTime=defaultdict(tuple)
        default_value = lambda: [0,0]
        self.stationStay= defaultdict(default_value)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        
        self.checkInTime[id]=(stationName , t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        inTime=self.checkInTime[id][1]
        startStation= self.checkInTime[id][0]
        endStation=stationName
        self.stationStay[(startStation,endStation)][0]+=(t-inTime)
        self.stationStay[(startStation,endStation)][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        return self.stationStay[(startStation,endStation)][0]/self.stationStay[(startStation,endStation)][1]

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)