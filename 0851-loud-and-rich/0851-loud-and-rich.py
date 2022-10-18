class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        
        
        n=len(quiet)
        
        richerthan={i:[i] for i in range(n)}
        indegree={i:0 for i in range(n)}
        for rich in richer:
            
            richerthan[rich[0]].append(rich[1])
            indegree[rich[1]]+=1
        
        queue=collections.deque()
        
        for person in indegree:
            if indegree[person]==0:
                queue.append(person)
        
        self.answer=[i for i in range(n)]
        while queue:
            richperson=queue.popleft()
            
            for neighbor in richerthan[richperson]:
                
                if quiet[self.answer[neighbor]]>quiet[self.answer[richperson]]:
                    self.answer[neighbor]=self.answer[richperson]
                               
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return self.answer
            
            
            
            
            