class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        
        
        
        imageOne1=[]
        imageTwo1=[]
        
        
        for i in range(len(img1)):
            
            for j in range(len(img2)):
                
                
                if img1[i][j]:
                    imageOne1.append((i,j)) 
                
                if img2[i][j]:
                    imageTwo1.append((i,j))
                
                
        pixels=defaultdict(int)
        pixels[None]=0
        for x1,y1, in imageOne1:
            for x2,y2, in imageTwo1:

                pixels[(x2-x1,y2-y1)]+=1
                
        return max(pixels.values())
                    
        
                    
                    
                
                
                    
                
                
                