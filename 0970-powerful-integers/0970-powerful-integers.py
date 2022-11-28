class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        
        ret=set()
        
        a=1
        b=1
        
        while a<bound:
            
            while b+a<=bound:
                
                ret.add(a+b)
                if y==1:
                    break
                b*=y
            
            if x==1:
                break
            
            a=a*x
            b=1
            
        return ret