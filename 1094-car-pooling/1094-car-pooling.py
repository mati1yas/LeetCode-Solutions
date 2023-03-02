class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        prefix=[0 for _ in range(1002)]
        
        
        
        for passengers,start,end in trips:
            
            prefix[start]+=passengers
            prefix[end]-=passengers
        
        
        if prefix[0]>capacity:
            return False
        for i in range(1,len(prefix)):
            
            prefix[i]+=prefix[i-1]
            
            if prefix[i]>capacity:
                return False
        return True