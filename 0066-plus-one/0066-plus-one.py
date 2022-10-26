class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        total=1
        n=len(digits)-1
        
        for digit in (digits):
            total+=10**n*digit
            n-=1
       
        arr=[]
        while total:
            rem=total%10
            arr.insert(0,rem)
            total//=10
        return arr
            
            