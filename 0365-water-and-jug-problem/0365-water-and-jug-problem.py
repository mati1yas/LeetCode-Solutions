class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        
        
        x=jug1Capacity
        y=jug2Capacity
        
        z=targetCapacity
        if x>y:
            x,y=y,x
        if x+y<z:
            return False
        
        queue=collections.deque()
        
        queue.append((0,0))  # start from empty jugs
        visited=set({(0,0)})
        
        while queue:
            
            curJ1,curJ2=queue.popleft()
            
            if curJ1+curJ2==z:
                return True
            operations=set()
            
            
            operations.add((x,curJ2))   # fill jug 1
            operations.add((curJ1,y))   # fill jug2 
            operations.add((0,curJ2))   # empty jug1
            
            operations.add((curJ1,0))   # empty jug2
            operations.add((0 if curJ1+curJ2<y else curJ1-(y-curJ2) ,min(y,curJ1+curJ2)))   # pour jug1 to jug2
            operations.add((min(x,curJ1+curJ2),0 if curJ2<x-curJ1 else curJ2-(x-curJ1) ))   # pour jug2 to jug1
            
            for newState in operations:
                if newState not in visited:
                    queue.append(newState)
                    visited.add(newState)
            
            
        return False
            
            
            
            
            
            
            
            
            
            
            