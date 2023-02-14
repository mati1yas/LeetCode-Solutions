
from itertools import permutations
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        powers=set()
        
        num=1
        powers.add(1)
        while num<=pow(10,9):
            num*=2
            powers.add(num)
        
        
        
        for num in list(permutations(str(n))):
            
            if num[0]!="0"   and int(''.join(num)) in powers:
                
                return True
        return False