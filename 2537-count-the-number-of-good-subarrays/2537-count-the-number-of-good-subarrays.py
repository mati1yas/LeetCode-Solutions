class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        
        
        calcArth = lambda x: (x*(x-1))//2
        
        
        count = defaultdict(int)
        n = len(nums)
        l = 0
        
        totalPairs = 0
        validAns=0
        for r in range(n):
            count[nums[r]] +=1
            
            
            diff= calcArth(count[nums[r]])-calcArth(count[nums[r]]-1)
            
            
            totalPairs += diff
            
            while totalPairs >= k:
                
                
                validAns+=1
                
                validAns+=len(nums)-r-1
                
                
                
                diff= calcArth(count[nums[l]])-calcArth(count[nums[l]]-1)
                
                count[nums[l]] -= 1
                
                
                totalPairs -= diff
                
                l+=1
                
        return validAns
                
                
             