class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        
        
        nums.sort()
        
        count=0
        for i in range(len(nums)):
            first=nums[i]
            if not first:
                continue
            for j in range(i+1,len(nums)):
                
                second = nums[j]
                if not second :
                    continue
                
                left= 0
                right= len(nums)-1
                ans=0
                while left<=right:
                    
                    mid=(left+right)//2
                    third=nums[mid]
                    
                    if first+second>third:
                        left=mid+1
                        
                    else:
                        right=mid-1
                
                count+=left-j-1
                        
                
        return count
                
                
                