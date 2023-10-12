class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        self.memo=[False for _ in range(n+1)]
        
        
        for stones in range(n+1):
            
            for pick in range(1,int(math.sqrt(stones))+1):
                
                if not self.memo[stones-(pick*pick)]:
                    self.memo[stones]=True
                    break
        return self.memo[-1]
    
        