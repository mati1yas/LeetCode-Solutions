class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        
        d=defaultdict(int)
        
        onesFromImage1=[]
        onesFromImage2=[]
        
        
        for r in range(len(img1)):
            for c in range(len(img2)):
                
                if img1[r][c]:
                    onesFromImage1.append((r,c))
                
                if img2[r][c]:
                    onesFromImage2.append((r,c))
                    
        
        d[None]=0
        for x1,y1 in onesFromImage1:
            for x2,y2 in onesFromImage2:
                
                
                d[(x2-x1,y2-y1)]+=1
                
                
        return max(d.values())
        
        
                