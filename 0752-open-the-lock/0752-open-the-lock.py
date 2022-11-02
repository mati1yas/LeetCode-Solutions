class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def generateKeys(current):
            ret=[]
            for i in range(len(current)):
                
                val=int(current[i])
                
                for change in (-1,1):
                    n=(val+change)%10
                    
                    ret.append(current[0:i]+str(n)+current[i+1:])
                
            return ret                
        
        queue= collections.deque()
        queue.append(('0000',0))       
        
        deadends=set(deadends)
        visited=set({'0000'})
        while queue:
            
            current,dist=queue.popleft()
            
            
            
            if current==target:
                
                return dist 
            if current in deadends:
                continue
            
            for newKey in generateKeys(current):
                
                if newKey not in visited:
                    queue.append((newKey,dist+1))
                    visited.add(newKey)
                
                
                
                
            
        return -1
            
            
            
        