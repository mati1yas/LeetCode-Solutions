class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        self.memo={}
        def getMaxUncrossed(i,startFrom):
            
            if i >= len(nums1) or  startFrom >= len(nums2):
                
                return 0
            
            
            if (i,startFrom)  in self.memo:                
                return self.memo[(i,startFrom)]
            
            
            
            m=getMaxUncrossed(i+1,startFrom)
            
            for j in range(startFrom , len(nums2)):
                if nums2[j]==nums1[i]:
                    m= max(m,getMaxUncrossed(i+1,j+1)+1)
             
            self.memo[(i,startFrom)]=m
            return m
        
        
        return getMaxUncrossed(0,0)
            
            
            