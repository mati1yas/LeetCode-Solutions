class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        
        
        citations.sort(reverse=True)
        h_index=0
        for i in range(len(citations)):
            if i<citations[i]:
                h_index=i+1
                
        return h_index
                
