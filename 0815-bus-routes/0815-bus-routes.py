class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        
        indexLocations =defaultdict(list)
        
        
        for i,route in enumerate(routes):
            
            for idx,r in enumerate(route):
                indexLocations[r].append(i)
        
        adjacency=defaultdict(list)
        
       
        
        queue=collections.deque()
        queue.append((source,0))  # start , steps
        visited=set()
        visitedIndexes=set()
        visited.add(source)
        
        while queue:
            
            node,steps=queue.popleft()
            
            if node==target:
                return steps
            
            for nbrIndex in indexLocations[node]:
                
                if nbrIndex in visitedIndexes:
                    continue
                visitedIndexes.add(nbrIndex)
                
                
                for nbrBus in routes[nbrIndex]:               
                
                
                    if nbrBus not in visited:
                        visited.add(nbrBus)
                        queue.append((nbrBus,steps+1))
                
                    
        return -1
                    
            
            
            
            
            
            
                