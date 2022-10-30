class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        layer=1
        total=1
        
        while True:
            
            
            layer=layer+1
            total+=layer
            
            if total==n:
                return layer
            if total>n:
                return layer-1
            