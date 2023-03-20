class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        last=float('-inf')
        Failed=False
        
        for i in range(len(flowerbed)):
            
            if flowerbed[i]==1:
                if i-last<2:
                    n+=1
                last=i
            
            elif n!=0 and i-last>=2:
                last=i
                n-=1
                
        
        return n==0
                
        
                