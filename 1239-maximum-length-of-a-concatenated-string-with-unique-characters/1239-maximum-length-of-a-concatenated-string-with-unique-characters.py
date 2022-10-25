class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        self.long=0
        def concatenate(l,curSub,curindex):
            
            
            self.long=max(self.long,l)
                
                
                
            
            for i in range(curindex+1,len(arr)):
                notUnique=False
                visited=set()
                for char in arr[i]:
                    
                    if char in curSub or char in visited:
                        notUnique=True
                        break
                    visited.add(char)
                    
                        
                if not notUnique:
                    concatenate(l+len(arr[i]),curSub|set(arr[i]),i)
        concatenate(0,set(),-1)
        return self.long
        
            