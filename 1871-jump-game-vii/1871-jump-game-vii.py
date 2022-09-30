class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        queue=collections.deque()
        max_reached=0
        queue.append(0)
        
        while queue:
            curidx=queue.popleft()
            
#             to check possible jump positions
            if curidx==len(s)-1:
                return True
            start=max(curidx+minJump,max_reached+1)
            end=min(curidx+1+maxJump,len(s))
            for x in range(start,end):
                if s[x]=="0":
                    queue.append(x)
            
            max_reached=curidx+maxJump
        return False