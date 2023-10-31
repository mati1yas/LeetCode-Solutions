class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        
        
        frequency= Counter(nums)
        
        smallFreq = min(frequency.values())
        
        
        smallFreq+=1
        
        
       
        result= float('inf')
        
        
        def canPartition(size):
            nextSize=size+1
            
            totalGroups=0
            for freq in frequency.values():
                
                formalGroups= freq//nextSize
                leftOver=freq%nextSize
                
                
                if leftOver ==0 :
                    
                    totalGroups+=formalGroups
                elif formalGroups>=size-leftOver:
                
                    totalGroups+=formalGroups+1
                
                else:
                    return float('inf')
                
            return totalGroups
        
                    
            
            
        
        
        for size in range(1, smallFreq):
            
            result=min(result,canPartition(size))
        
        return result
        
        