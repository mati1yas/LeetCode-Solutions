class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        
        
        champagne=[[0] * k for k in range(1, 102)]
        champagne[0][0]=poured
        
        for level in range(query_row+1):
            
            for glass in range(level+1):
                
                
                overflow=(champagne[level][glass]-1)/2
                
                
                if overflow>0:
                    champagne[level+1][glass]+=overflow
                    champagne[level+1][glass+1]+=overflow
        
        return min(1,champagne[query_row][query_glass])
                
                
        
        
        