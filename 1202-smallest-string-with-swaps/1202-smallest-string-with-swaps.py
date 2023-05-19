class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        
        self.parent = { i: i for i in range(len(s))}
        
        self.chars={ i : [s[i]] for i in range(len(s))}
        self.size = { i : 1 for i in range(len(s))}


        def find(char):
            
            if self.parent[char]!=char:                
                self.parent[char]=find(self.parent[char])
                
            return self.parent[char]
        
        
        def union(char1,char2):
            
            pc1,pc2 = find(char1),find(char2)
            
            
            if pc1!= pc2:
                
                if self.size[pc1]>self.size[pc2]:
                
                   
                    self.parent[pc2]=pc1
                    self.size[pc1]+=self.size[pc2]
                    
                    self.chars[pc1].extend(self.chars[pc2])
                else:
                    self.size[pc2]+=self.size[pc1]
                    
                    self.chars[pc2].extend(self.chars[pc1])
                    self.parent[pc1]=pc2
                    
        
        
        for a,b in pairs:
            union(a,b)
       
    
        ans=''
        
        newChars={}
        
        for key , l in self.chars.items():
            newChars[key]=sorted(l,reverse=True)
        
        
        for i in range(len(s)):
            par=find(i)
            ans+=newChars[par].pop()
        return ans
        
        
        
        
            