class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        
        
        right=0
        left=0
        
        freq=defaultdict(int)
        minOp=float('inf')
        
        while right<len(blocks):
            
            while right<len(blocks) and right-left+1<=k:
                
                freq[blocks[right]]+=1
                right+=1
            
            
            minOp=min(minOp,freq["W"])
            freq[blocks[left]]-=1
            left+=1
        return minOp
                
                