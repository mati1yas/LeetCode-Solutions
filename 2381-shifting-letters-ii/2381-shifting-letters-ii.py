class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        changes=[0 for i in range(len(s)+1)]
        
        
        for start,end,dirc in shifts:            
            if dirc==1:
                changes[start]+=1
                changes[end+1]-=1
                           
            else:
                changes[start]-=1
                changes[end+1]+=1
        
        prefix=[changes[0]]
        
        for change in changes[1:]:
            prefix.append(prefix[-1]+change)
        
        
        for i, char in enumerate(s):
            
            newOrd=ord(char)+prefix[i]%26
            newOrd-=26 if newOrd>122 else 0
            s=s[0:i] + chr(newOrd) +s[i+1:]
        return s