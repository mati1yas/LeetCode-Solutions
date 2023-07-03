class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        count=0
        
        if len(s)!=len(goal):
            return False
        
        
        
                
        indexes=[]
        for i in range(len(s)):
            
            if s[i]!=goal[i]:
                indexes.append(i)
                count+=1
            
            if count >= 3:
                
                return False
        if count==1:
            return False
        if count==0:
            
            # if s == goal:
            frequency=defaultdict(int)
            for char in s:
                frequency[char]+=1
            
                if frequency[char]==2:
                    return True
                
            return False
        return s[indexes[0]]==goal[indexes[1]] and s[indexes[1]]==goal[indexes[0]] 
            
            