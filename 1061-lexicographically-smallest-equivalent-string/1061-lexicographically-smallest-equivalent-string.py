class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        parent=dict()
        
        for x in range(97 ,123):
            parent[chr(x)]=chr(x)       
       
        
        
        def find(parent,char):
            
            if parent[char]!=char:
                parent[char]=find(parent,parent[char])
            return parent[char]
        
        def union(parent,char1,char2):            
            p1,p2=find(parent,char1),find(parent,char2)
            
            if p1!=p2 :
                if p1<p2:
                    parent[p2]=p1
                else:
                    parent[p1]=p2
           
        
        for i in range(len(s1)):
            union(parent,s1[i],s2[i])
            
        smallestString=''
        
        for char in baseStr:
            smallestString+=find(parent,char)
        return smallestString
        
        
        
        