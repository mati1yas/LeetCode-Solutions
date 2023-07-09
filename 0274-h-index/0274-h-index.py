class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        citations.sort(reverse=True)
        
        
        
        for idx,cit in enumerate(citations):
            if idx+1>cit:
                return idx
        return len(citations)