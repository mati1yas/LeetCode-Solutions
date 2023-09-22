class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        
        
        wantsToBeWith = {
            
            
        }
        
        
        
        
        for first , second in pairs:
            
            
            wantsToBeWith[first]=preferences[first][:preferences[first].index(second)]
            wantsToBeWith[second]=preferences[second][:preferences[second].index(first)]
            
            
            
        
        count=0
        for first  in wantsToBeWith:
            
            for second in wantsToBeWith[first]:
                
                if first in wantsToBeWith[second]:
                    count+=1
                    break
        return count
                
        
        
            
            
        