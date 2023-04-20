class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        
        
        graph=defaultdict(list) 
        
        
        for start,end in edges:
            
            graph[start].append(end)            
            graph[end].append(start)
            
             
            
        self.bobPath={}
        self.found=False
        visited=set()
        def bobMoving(node,dist):
            
            self.bobPath[node]=dist
            visited.add(node)
            
            if node==0:
                self.found=True
                return True
            
            
            for nbr in graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    if not self.found:
                        bobMoving(nbr,dist+1)
                    else:
                        return
                    
                    
            if not self.found:
                del self.bobPath[node]
                
        
        
        bobMoving(bob,0)
        
        visitedAlice=set({0})
        alicePath=defaultdict(int)
        
        self.maxNetIncome=float('-inf')
        def aliceMoving(node,dist,income):
            
           
            cost_reward=0
            
            if node not in self.bobPath:
                cost_reward=amount[node]
            elif dist==self.bobPath[node]:
                cost_reward=amount[node]/2
                
            
            elif dist<self.bobPath[node]:
                
                cost_reward=amount[node]
            
                  
            leaf=True
            for nbr in graph[node]:
        
                if nbr not in visitedAlice:
                    leaf=False
                    
            if leaf:
               
                self.maxNetIncome=max(self.maxNetIncome,income+cost_reward)
                    
            
            for nbr in graph[node]:
        
                if nbr not in visitedAlice:
                    visitedAlice.add(nbr)
                    aliceMoving(nbr,dist+1,income+cost_reward)
            
            
            
        aliceMoving(0,0,0)
        
        
        return int(self.maxNetIncome)
        
        
        
        
        