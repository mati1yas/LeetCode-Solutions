class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        
        total = 0
        
        notes=defaultdict(int)
        
        for bill in bills:
            
            change=bill-5
            
            if change==5:
                
                if notes[5]>0:
                    notes[5]-=1
                else:
                    return False
                    
            
            elif change==10:
                
                if notes[10]>0:
                    notes[10]-=1
                elif notes[5]>=2:
                    notes[5]-=2
                else:
                    return False
                
                
                
            elif change==15:
                if notes[10]>0 and notes[5]:
                    notes[10]-=1
                    notes[5]-=1
                elif notes[5]>=3:
                    notes[5]-=3
                else:
                    return False
            
            
            notes[bill]+=1
                
        return True