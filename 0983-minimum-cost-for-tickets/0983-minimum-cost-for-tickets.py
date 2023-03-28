class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        
        self.memo={}
        def buyTickets(index,covered,cost):
            
            
            if index==len(days):
                
                return 0
            
            
            if (index) in self.memo:
               
                return self.memo[index]
            
            minr=0
            
            
            oneDay=buyTickets(index+1,covered.union(set([i for i in range(days[index],days[index]+1)])),cost+costs[0])+costs[0]

            i=index
            while i <len(days) and days[i]<days[index]+7:
                i+=1

            sevenDay=buyTickets(i,covered.union(set([i for i in range(days[index],days[index]+7)])),cost+costs[1])+costs[1]

            i=index
            while i <len(days) and days[i]<days[index]+30:
                i+=1

            thirtyDay=buyTickets(i,covered.union(set([i for i in range(days[index],days[index]+30)])),cost+costs[2])+costs[2]


            minr=min(oneDay,sevenDay,thirtyDay)

            
            
            
            self.memo[index]=minr
                
            return minr
             
        return buyTickets(0,set(),0)
        