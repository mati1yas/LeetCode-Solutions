class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:


        
        
        taskFrequency=Counter(tasks)        
        minRounds=0
        
        
        
        for frequency in taskFrequency.values():
            
            if frequency==1:
                return -1
            
            if frequency%3==0:
                minRounds+=frequency//3
            else:
                minRounds+=frequency//3+1
                
            
            
        return minRounds
