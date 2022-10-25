class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans=[]
        for number in nums:
        
            if nums[abs(number)-1]<0:
                ans.append(abs(number))
            else:
                nums[abs(number)-1]*=-1
    
        return ans