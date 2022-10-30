class Solution:
    def secondHighest(self, s: str) -> int:
        digits=[]
        visited=set()
        for char in s:
            if char.isdigit() and char not in visited:
                digits.append(int(char))
                visited.add(char)
        
        digits.sort()
        
        return digits[-2] if len(digits)>=2 else -1