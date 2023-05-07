class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        
        
        
        tiles.sort()
        
        prefix= [0]+list(itertools.accumulate(r-l+1 for l,r in tiles))
        
        
        ends = [e for i ,e in tiles]
        
        n= len(tiles)
        
        j=0
        
        ans = 0
        
        
        for i in range(n):
            
            left = tiles[i][0]
            
            right = min(ends[-1], left + carpetLen - 1)
        
        
            while j < n and ends[j] < right:
                j+=1
                
            
            
#             the two cases will be covered

            
            if tiles[j][0] > right:
                ans = max(ans,prefix[j] - prefix[i])
                
            else:
                ans = max(ans, prefix[j+1]-prefix[i]-ends[j]+right)
                
            
        return ans
                
        
        