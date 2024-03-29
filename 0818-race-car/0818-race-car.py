class Solution:
    def racecar(self, target: int) -> int:
        
        
        
        queue=collections.deque()
        
        queue.append((0,0,1)) # count,position,speed
        
        while queue:
            count,curPos,speed=queue.popleft()
            
            if curPos==target:
                return count
            
            
            queue.append((count+1,curPos+speed,speed*2))
            
            
            
#             here we are changing direction in case the car is moving away from target
                # moving to right from the target             moveing  away to left from target 
            if (curPos+speed>target and speed>0 ) or (curPos+speed<target and speed<0):
                newSpeed=-1 if speed>0 else 1
                queue.append((count+1,curPos,newSpeed))
            
            
            
            