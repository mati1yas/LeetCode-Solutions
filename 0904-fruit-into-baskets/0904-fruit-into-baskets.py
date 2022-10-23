class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        freq=defaultdict(int)
        
        
        start=0
        end=0
        long=0
        while end<len(fruits):
            
            freq[fruits[end]]+=1
            
            while len(freq)>2:
                
                freq[fruits[start]]-=1
                if freq[fruits[start]]==0:
                    freq.pop(fruits[start])
                start+=1
                
            long=max(long,end-start+1)
            end+=1
        return long
            