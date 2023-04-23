class Solution:
    def minInsertions(self, s: str) -> int:
        
        
        # m b a d m
        #   |   |
            
            
        self.memo={}
        def insert(left,right):
            
            if left>=right:
                return 0
            if right<0 or left>=len(s):
                return 0
            
            if (left,right) in self.memo:
                
                return self.memo[(left,right)]
           
            r=0
            if s[left]!=s[right]:
                r=1+min(insert(left+1,right),insert(left,right-1))
            
            else:
                r= insert(left+1,right-1)
            
            self.memo[(left,right)]=r
            
            return r
        
        return insert(0,len(s)-1)
            
            
            
        
        
        