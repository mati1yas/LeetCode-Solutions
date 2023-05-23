
class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        self.parent={i:i for i in range(1000+1) }
        self.size={i:1 for i in range(1000+1)}
        
        def find(node):
            
            if self.parent[node]!=node:
                self.parent[node]=find(self.parent[node])
                
            
            return self.parent[node]
        
        
        
        def union(node1,node2):
            
            par1,par2=find(node1),find(node2)
            
            
            
            if self.size[par1]>self.size[par2]:
                self.parent[par2]=par1
                self.size[par1]+=self.size[par2]
                
            else:
                self.parent[par1]=par2
                
                self.size[par2]+=self.size[par2]
                
        
        
        
        ans = []
        
        for x,y in requests:
            
            
            
            xpar1,ypar2=find(x),find(y)
            
            canBeFrnds=True
            for a,b in restrictions:
                apar1,bpar2=find(a),find(b)
                
                if set([xpar1,ypar2])== set([apar1,bpar2]):
                    
                    canBeFrnds=False
                    break
            ans.append(canBeFrnds)
            
            if canBeFrnds:
                union(x,y)
                
        
        
        return ans
        
                
        
        