class Solution:
    def minDeletions(self, s: str) -> int:
        freq=Counter(s)
        freq_list=list(freq.values())
        freq_list.sort()
   
        visited=set()
        last=freq_list[-1]
        visited.add(freq_list[-1])
        print(freq_list)
        cost=0
        for i in range(len(freq_list)-2,-1,-1):

            cur=freq_list[i] 
            
            if cur in visited:

                if cur==last:
                    cost+=1

                    last=cur-1
                    visited.add(last)
                    
                    
                    
                elif last<cur:
                    
                    

                    if last>1:
                        cost+=  cur-(last-1)
                        last-=1
                    else:
                        cost+=cur
                        last=1
                    visited.add(last)
            else:
                visited.add(cur)
                last= cur
                
        return cost