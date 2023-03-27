class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        total=0
        pick=min(numOnes*1,k*1)
        total+=pick
        k-=pick
        
        if not k:
            return total
        
        pick=min(numZeros,k)
        total+=pick*0
        k-=pick

        if not k:
            return total
        pick=min(numNegOnes,k)
        total+=pick*-1
        k-=pick
        return total
        

            
            
        