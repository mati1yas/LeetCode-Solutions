class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        
        p1=0
        p2=0
        
        m=float('-inf')
        pre=0
        cost=0
        
        while p2<len(colors):
            
            if colors[p2]!=colors[p1]:
                cost+=pre-m
                pre=0
                p1=p2
                m=float('-inf')
            
            pre+=neededTime[p2]
            m=max(m,neededTime[p2])
            p2+=1
            
        cost+=pre-m
        return cost
            
                
        