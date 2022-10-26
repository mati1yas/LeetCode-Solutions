class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        numerics={
            "1":1,
            "0":0,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
        }
        
        def convert(num,numerics):
            number=0
            n=len(num)-1
            for char in num:
                number+=10**n*numerics[char]
                n-=1
            return number
        number1=convert(num1,numerics)
        number2=convert(num2,numerics)
        product=number1*number2
        
        
            
            
        
        
        return str(product)