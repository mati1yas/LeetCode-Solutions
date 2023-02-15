class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left   = 0
        right  = 0
        
        for char in s:
            
           
            left += 1 if char == '(' else -1
            
            right += 1 if char != ')' else -1
            if right < 0: break
            left = max(left, 0)

        return left == 0