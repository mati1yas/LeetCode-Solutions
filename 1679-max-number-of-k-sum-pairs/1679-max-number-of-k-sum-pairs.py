class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        print(nums)
        nums.sort()
        left=0
        right=len(nums)-1
        
        
        count=0
        while left<right:
            
            if nums[left]+nums[right]<k:
                left+=1
            elif nums[left]+nums[right]>k:
                right-=1
                
                
            elif nums[left]+nums[right]==k:
                left+=1
                right-=1
                count+=1
        return count
        
        
        return 0