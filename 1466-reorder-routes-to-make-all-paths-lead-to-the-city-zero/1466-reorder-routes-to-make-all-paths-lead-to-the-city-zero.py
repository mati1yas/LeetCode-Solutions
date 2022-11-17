class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        queue=collections.deque()
        visited=set()
        
        goto=defaultdict(list)
        comefrom=defaultdict(list)
        
        for a,b in connections:
            goto[a].append(b)
            comefrom[b].append(a)
        
        queue.append(0)
        roads=0
        while queue:
            
            for i in range(len(queue)):
                node=queue.popleft()
                visited.add(node)
                for goNode in goto[node]:
                    if goNode not in visited:
                        roads+=1
                        queue.append(goNode)
                for comeNode in comefrom[node]:
                    if comeNode not in visited:
                        queue.append(comeNode)
        return roads 