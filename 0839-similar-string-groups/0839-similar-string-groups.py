class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        
        
        
        def checkSimilarity(word1,word2):
            diff=0
            for k in range(len(word1)):
                if word1[k]!=word2[k]:
                    diff+=1

            return  diff==0 or diff==2
        graph=defaultdict(list)
        
        
        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if len(strs[i])!=len(strs[j]):
                    continue
                if checkSimilarity(strs[i],strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)
                    
        
       
                    
        visited=set()
        
        
        def dfs(node):
            visited.add(node)
            
            for nbr in graph[node]:
                if nbr not in visited:                    
                    dfs(nbr)
            
        
    
        count=0
        for i in range(len(strs)):
            if i not in visited:
                dfs(i)
                count+=1
                
            
        return count
                
                    
                    
                    
            