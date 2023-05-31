class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        
        subsequence= defaultdict(int)
        
        large_subsequence=0
        for val in arr:
            
            
            prev=val-difference
            
            subsequence[val]=1+subsequence[prev]
            large_subsequence=max(large_subsequence,subsequence[val])
            
            
        return large_subsequence