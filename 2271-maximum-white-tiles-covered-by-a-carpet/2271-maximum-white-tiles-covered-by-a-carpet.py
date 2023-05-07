class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        
        
        
        tiles.sort()
        
        prefix= [0]+list(itertools.accumulate(r-l+1 for l,r in tiles))
        
        
        ends = [e for i ,e in tiles]
        
        n= len(tiles)
        
        j=0
        
        ans = 0
        
        
        for i in range(n):
            
            left = tiles[i][0]    # we are always assuming that start of our window lies in at the start of a range. 
            
            right = min(ends[-1], left + carpetLen - 1)

            while j < n and ends[j] < right:
                j+=1
               
#             the two cases will be covered

            
            if tiles[j][0] > right: # case where end of window does not lie in the current range being considered 
                ans = max(ans,prefix[j] - prefix[i])
                
            else:  # case where end of the window lies 
                ans = max(ans, prefix[j+1]-prefix[i]-ends[j]+right)
                
            
        return ans
                
        
        