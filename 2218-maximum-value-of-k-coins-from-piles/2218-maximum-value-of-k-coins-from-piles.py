class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        
        self.memo={}
        def takeCoin(pileIdx,coinsToTake):
            
            
            if pileIdx==len(piles) or coinsToTake==0:
                return 0
            
            
            if (pileIdx,coinsToTake) in self.memo:
                
                return self.memo[(pileIdx,coinsToTake)]
            
            takeVariations=takeCoin(pileIdx+1,coinsToTake)
            
            totalCoins=0
            for i in range(min(coinsToTake,len(piles[pileIdx]))):
                
                totalCoins+=piles[pileIdx][i]
                
                takeVariations=max(takeVariations,totalCoins+takeCoin(pileIdx+1,coinsToTake-(i+1)))
                
                
            self.memo[(pileIdx,coinsToTake)]=takeVariations
                
            return takeVariations
        
        return takeCoin(0, k)
            