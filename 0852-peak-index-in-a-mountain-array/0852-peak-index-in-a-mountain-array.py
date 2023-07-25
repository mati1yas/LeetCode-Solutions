class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        
        stack = [ ]
        
        index=0
        for num in arr:
            index+=1
            
            if stack and stack[-1]>num:
                return index-2
            stack.append(num)
                