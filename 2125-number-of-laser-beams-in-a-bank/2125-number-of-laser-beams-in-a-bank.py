class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        
        beams=0
        last=0
        for i in range(len(bank)):
            count=0
            for cell  in bank[i]:
                
                if cell=="1":
                    count+=1
                    
            
            if count!=0:
                beams+=last*count
                last=count
                
                
        return beams
            
                    
        