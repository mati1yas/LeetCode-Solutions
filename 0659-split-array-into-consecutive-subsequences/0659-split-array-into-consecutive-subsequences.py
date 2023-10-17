class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        
        frequency = Counter(nums)
        
        need = defaultdict(int)
        
        
        
        
        for num in nums:
            
            
            if not frequency[num] :
                continue
                
            
            if need [num]>0:
                frequency[num]-=1
                need[num]-=1
                need[num+1]+=1
            
            
            elif  frequency[num]>0 and frequency[num+1]>0 and frequency[num+2]>0:
                
                frequency[num+1]-=1
                frequency[num+2]-=1
                frequency[num]-=1
                
                need[num+3]+=1
                
            else:
                return False
        return True