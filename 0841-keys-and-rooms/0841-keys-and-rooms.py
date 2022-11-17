class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        queue=collections.deque()
        visited=set()
        
        canOpen={}
        for idx,room in enumerate(rooms):
            canOpen[idx]=room
        
        queue.append(0)
        
        while queue:
            
            cur=queue.popleft()
            visited.add(cur)
            for nbr in canOpen[cur]:
                
                if nbr not in visited:
                    queue.append(nbr)
        
        for i in range(len(rooms)):
            if i not in visited:
                return False
        return True