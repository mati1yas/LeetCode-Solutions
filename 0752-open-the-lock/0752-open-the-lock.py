class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        
        queue= collections.deque()
        queue.append(('0000',0))
        
        
        visited=set({'0000'})
        while queue:
            
            current,dist=queue.popleft()
            
            
            if current==target:
                
                return dist 
            if current in deadends:
                continue
            
            for i,key in enumerate(current):
                prev=key
                
                
                if int(key)==9:
                    up=0
                else:
                    up=int(prev)+1
                
                
                newKey=current[0:i]+str(up)+current[i+1:]
                if newKey not in visited:
                    queue.append((newKey,dist+1))
                    visited.add(newKey)
                
                
                
                
                if int(key)==0:
                    down=9
                else:
                    down=int(prev)-1
                newKey=current[0:i]+str(down)+current[i+1:]
                if newKey not in visited :
                    queue.append((newKey,dist+1))
                    visited.add(newKey)
                
                
            
        return -1
            
            
            
        