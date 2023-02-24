class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        activeMinutes=defaultdict(set)
        
        for uid,minute in logs:
            
            activeMinutes[uid].add(minute)
            
        ans=[0 for _ in range(k)]
        
        for key in activeMinutes:
            
            ans[len(activeMinutes[key])-1]+=1
        return ans