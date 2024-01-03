class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        print(len(bank))
        new_bank=[]
        for idx,row in enumerate(bank ):
            
            count=0 
            for cell in row:
                
                if cell=="1":
                    count+=1
                    
            if count!=0:
                new_bank.append(row)
                
        bank = new_bank
        row_device_counts = {}
        
        for idx,row in enumerate(bank ):
            
            count=0 
            for cell in row:
                
                if cell=="1":
                    count+=1
                    
            row_device_counts[idx] = count
            
        beams=0
        for i in range(len(bank)-1):
            beams+=row_device_counts[i]*row_device_counts[i+1]
            
        return beams
            
                    
        