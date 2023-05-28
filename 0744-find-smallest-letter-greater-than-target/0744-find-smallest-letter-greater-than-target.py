class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        
        ans=None
        for char in letters:
            if char > target:
                ans= char
                
                break
                
        return ans if ans else letters[0]
                
        
        