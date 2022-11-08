class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
       
        choices=[i for i in range(1,maxChoosableInteger+1)]
        played={}
        
        total=(maxChoosableInteger+1)*maxChoosableInteger/2
        if total<desiredTotal:
            return False
        def playGame(choices,remaining):
            
            if choices[-1]>=remaining:
                return True
            
            
            curGame=tuple(choices)
            
            if curGame in played:
                return played[curGame]
            
            
            for idx in range(len(choices)):                
                if not playGame(choices[:idx]+choices[idx+1:],remaining-choices[idx]):
                    played[curGame]=True
                    return True
                
                
            played[curGame]=False
            return False
        
        return playGame(choices,desiredTotal)
                
                
            
            
            
            
        
        