class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        
        
        
        frequency=Counter(changed)
        
        changed.sort()
        
        ans=[]
        
        if len(changed)%2!=0:
            return []
        
        twice={}
        
        
        for num in changed:
            
            twice[num]=num*2
        
        for num in changed:
            
            
            if num in frequency and twice[num] in frequency:
                frequency[num]-=1
                if frequency[twice[num]]:
                    frequency[twice[num]]-=1
                else:
                    return []
                
                if frequency[num]==0:
                    frequency.pop(num)
                
                if twice[num] in frequency and frequency[twice[num]]==0:
                    frequency.pop(twice[num])
                elif twice[num] not in frequency and twice[num]!=num:
                    return []
                    
                ans.append(num)
            
                
                
        return ans if len(ans)*2==len(changed) else []
                