class Solution:
    def partitionString(self, s: str) -> int:
        
        
        frequency=Counter(s)
        
        distinct=set()
        count=1
        for char in s:
            
            if char in distinct:
                count+=1
                distinct=set()
            distinct.add(char)
        return count
            
            