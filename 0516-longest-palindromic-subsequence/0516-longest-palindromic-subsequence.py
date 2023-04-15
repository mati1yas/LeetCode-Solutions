class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        
        
        longest=0
        
        self.memo={}
        def sub(left,right):
            
            
            if left>right:
                return 0
            
            if left==right:
                return 1
            
            
            if (left,right) in self.memo:
                
                return self.memo[(left,right)]
            
            
            if s[left]==s[right]:
            
                self.memo[(left,right)]=2+sub(left+1,right-1)
            
            else:
                self.memo[(left,right)]=max(sub(left+1,right),sub(left,right-1))
                
                
            return self.memo[(left,right)]
        
        
        
        return sub(0,len(s)-1)
            
            
            
       
        
            
            
            