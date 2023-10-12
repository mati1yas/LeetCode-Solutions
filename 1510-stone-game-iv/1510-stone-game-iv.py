class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        self.memo={0: False}
        def pickStone(stones):
            
         
            if stones in self.memo:
                return self.memo[stones]
            
            for pick in range(1,int(math.sqrt(stones))+1):
                
                if not pickStone(stones-(pick*pick)):
                    self.memo[stones]=True
                    return True
                
            self.memo[stones]=False
            return False
        
        return pickStone(n)