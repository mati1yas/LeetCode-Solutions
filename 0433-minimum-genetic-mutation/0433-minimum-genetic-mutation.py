class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        visited=set({start})
        
        queue=collections.deque()
        queue.append((start,0))
        bank=set(bank)
        while queue:
            
            currentGene,steps=queue.popleft()
            
            if currentGene == end:
                return steps
            
            for idx,gene in enumerate(currentGene):
                
                for change in ('A','C','G','T'):
                    
                    newGene=currentGene[0:idx]+change + currentGene[idx+1:]
                    
                    if newGene in bank and newGene not  in visited:
                        queue.append((newGene,steps+1))
                        visited.add(newGene)
                        
        return -1
                        
                        
                    
                