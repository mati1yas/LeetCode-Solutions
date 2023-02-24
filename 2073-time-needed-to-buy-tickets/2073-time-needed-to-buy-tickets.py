class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        totalSeconds=0
        for i in range(100):
            stop=False
            for j in range(len(tickets)):
                
                if tickets[j]>0:
                    tickets[j]-=1
                
                    totalSeconds+=1
                if tickets[k]==0:
                    stop=True
                    break
            if stop:
                break
            
        return totalSeconds
                