class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        
        
        
        queue=collections.deque()
        farthest=max(x,max(forbidden))+a+b
        
        seen=set()
        queue.append((True,0))
        
        for forbid in forbidden:
            seen.add((True,forbid))
            seen.add((False,forbid))
        jumps=0
        while queue:
            
            for _ in range(len(queue)):
            
                curDir,curPos=queue.popleft()
                if curPos==x:
                    return jumps
                forward=(True,curPos+a)
                backward=(False,curPos-b)
                
                if forward not in seen and curPos+a<=farthest:
                    seen.add(forward)
                    queue.append(forward)
                
                if curDir and backward not in seen and curPos-b>0:
                    seen.add(backward)
                    queue.append(backward)
            jumps+=1
        return -1
                
        