class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        
        pre=[0]
        
        for alt in gain:
            
            pre.append(pre[-1]+alt)
        
        return max(pre)