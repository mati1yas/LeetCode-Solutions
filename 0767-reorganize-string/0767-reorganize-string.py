
import heapq as h
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        freq=Counter(list(s))
        
        letters=[]
        for let in freq:
            letters.append((-freq[let],let))
        
            
        
        h.heapify(letters)
        
        
        newS=""
        popped=""
        count=0
        while letters:
            
            curf,curl=h.heappop(letters)
            
            if newS and newS[-1]!=curl:
                newS+=curl
#                 have to reappend after decrementing the freq
                freq[curl]-=1
                if freq[curl]!=0:
                    h.heappush(letters,(-freq[curl],curl))
                if popped:
                    h.heappush(letters,(-freq[popped],popped))
                    popped =""
                    
                
                
                
            elif not newS: 
                newS+=curl
                freq[curl]-=1
                if freq[curl]!=0:
                    h.heappush(letters,(-freq[curl],curl))
                
            elif not popped:
                popped=curl 
            else:
                return ""
               
        
        if popped:
            return ""
        return newS
        
        
        
        
        