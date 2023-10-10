class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
       
        multi=60
        
        count=0
        
        multiples=[]
        while multi<=1000:
            
            multiples.append(multi)
            multi+=60
  
            
        visitedComplement=defaultdict(int)
        
        time.sort() 
        for t in time:
            for multi in multiples:
                
                if multi-t in visitedComplement:
                    count+=visitedComplement[multi-t]
            visitedComplement[t]+=1
            
        return count
            
        
        