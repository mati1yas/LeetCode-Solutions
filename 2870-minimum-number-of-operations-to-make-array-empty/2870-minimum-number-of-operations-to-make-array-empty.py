class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        
        frequency=Counter(nums)
        
        
        operations= 0 
        for freq in frequency.values():
            
            if freq%3==0:
                
                operations+=(freq//3)
                continue
            count=0
            while freq>=0:
                
                if freq%3!=0:
                    count+=1
                    freq-=2
                
                if freq%3==0:
                
                    operations+=(freq//3)
                    break
                    
                if freq<=0:
                    return -1
            operations+=count
            
        return operations