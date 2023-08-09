class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        
        nums.sort()
        
        def countValids(topDiff):
            
            index=0
            count=0
            
            while index<len(nums)-1:
                
                if nums[index+1]-nums[index]<=topDiff:
                    
                    count+=1
                    index+=1
                index+=1
                
                
            return count
        
        
        left,right=0,nums[-1]-nums[0]
        
        
        while left<=right:
            
            mid=left+(right-left)//2
            
            if countValids(mid)>=p:
                right=mid-1
                
            else:
                left=mid+1
                
        
        return left
                
                