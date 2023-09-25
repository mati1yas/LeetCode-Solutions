class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        start,end=intervals[0]
        
        mergedIntervals = []
        
        for s, e in intervals[1:]:
            
            if s<=end:
                end=max(e,end)
                
            else:
                mergedIntervals.append([start,end])
                start=s
                end=e
        mergedIntervals.append([start,end])     
        return mergedIntervals