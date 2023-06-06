class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        
        
        ans = [ ]
        if not nums:
            return nums
        start= nums[0]
        prev=start
        for num in nums:
            
            if prev+1<num:
                if start==prev:
                    ans.append(str(prev))
                else:
                    ans.append(str(start)+"->"+str(prev))
                start=num
                prev=start
            prev=num
        
        
        if start==prev:
            ans.append(str(prev))
        else:
            ans.append(str(start)+"->"+str(prev))
        
        return ans
            
            
            