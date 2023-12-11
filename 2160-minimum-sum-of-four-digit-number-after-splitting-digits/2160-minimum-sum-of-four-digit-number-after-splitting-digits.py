class Solution:
    def minimumSum(self, num: int) -> int:
        
        num1 = ""
        num2 = ""
        first=True
        
        num =  sorted(str(num))
        
        num1=num[0]+num[2]
        num2=num[1]+num[3]
        return int(num1)+int(num2)
        
        
        
            