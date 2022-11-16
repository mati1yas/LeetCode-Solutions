class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        
        perms=sorted(permutations(arr),reverse=True)
        
        for perm in perms:
            h1,h2,m1,m2=perm
            
            hour=h1*10+h2
            minute=m1*10+m2
            
            if hour<24 and minute<60:
                return f"{h1}{h2}:{m1}{m2}"
        
        return ""