class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        short_frequency=Counter(t)
        
        long_frequency=defaultdict(int)
        
        left = 0
        right = 0
        
        
        def valid():
            
            for key in short_frequency:
                
                if short_frequency[key]>long_frequency[key]:
                    return False
            return True
            
            
        
        length=float('inf')
        ans=''
        while right<len(s):
            
            
            if s[right] in short_frequency:
                long_frequency[s[right]]+=1
                
             
            while left<len(s) and right < len(s) and valid():
                
                if right-left+1<length:
                    ans=s[left:right+1]
                    length= right- left+1 
                    
                if s[left] in short_frequency:
                    long_frequency[s[left]]-=1 
                left+=1
            right+=1
        return ans
        