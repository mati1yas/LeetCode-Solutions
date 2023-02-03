
import random
class Solution:

    def __init__(self, w: List[int]):
        
        
        self.tot=sum(w)
        self.indexes=[i for i in range(len(w))]
        self.probabilityWeight=tuple([(w[i]/self.tot) for i in range(len(w))])
        

    def pickIndex(self) -> int:
      
        return random.choices(self.indexes,weights=self.probabilityWeight,k=1)[0]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()