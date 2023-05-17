class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        not_equal = []
        self.parent={chr(i):chr(i) for i in range(97,123)}
        def find(node):
            
            if self.parent[node] != node:
                
                self.parent[node]=find(self.parent[node])
            return self.parent[node]
        
        
        def union(equat):
            
            
            
            left= find(equat[0])
            right= find(equat[-1])
            
            if equat[1]=='=':
                for n in self.parent:
                    if self.parent[n]==left:
                        self.parent[n]=right
                        
                
            else:
                
                if find(left) == find(right):
                    print('from here')
                    return False
                else:
                    not_equal.append((left,right))
            
            
            return True
            
            
            
        for equation in equations:
            
            if not union(equation):
                
                return False
            
        for x,y in not_equal:
            if find(x) == find(y):
                return False
        return True