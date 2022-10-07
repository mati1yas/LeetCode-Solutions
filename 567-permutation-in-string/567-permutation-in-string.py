class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        freq=defaultdict(int)
        
        for ch in s1:
            freq[ch]+=1
        
        freq2=defaultdict(int)
        pre=0
        for i in range(len(s2)):
            
            if len(s1)==sum(freq2.values()):
                if s2[i-len(s1)] in freq2:
                    
                    freq2[s2[i-len(s1)]]-=1
                    if freq2[s2[i-len(s1)]]==0:
                        freq2.pop(s2[i-len(s1)])
            freq2[s2[i]]+=1
            
            if freq2==freq:
                return True
        return False
            
        
        