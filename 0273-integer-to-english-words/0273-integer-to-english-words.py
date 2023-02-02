class Solution:
    def numberToWords(self, num: int) -> str:
        
        oneToTen={
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
        
        tenData={
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
        
        tenToTwenty= {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
        
        
        
        
            
        
        def twoHelper(number):
            
            if not number:
                return ""
            
            if number<10:
                return oneToTen[number]
            elif number<20:
                return tenToTwenty[number]
            else:
                ten=number//10
                ones=number-ten*10
                
                if ones:
                    return tenData[ten]+ " "+oneToTen[ones]
                    
                else:
                    
                    return tenData[ten]
                    
        
        def threeHelper(number):
            
            hundred=number//100
            tens=number-hundred*100
            
            if hundred and tens:
                return oneToTen[hundred]+" Hundred "+ twoHelper(tens)
                    
            
            elif not hundred and tens:
                return twoHelper(tens)
            
            elif hundred and not tens:
                return oneToTen[hundred]+" Hundred"
            
            
        if not num:
            return "Zero"
 
        
        billion=num//1000000000
        million=(num-billion*1000000000)//1000000
        thousand=(num-billion*1000000000-million*1000000)//1000
        hundred=num-billion*1000000000-million*1000000-thousand*1000
        
        result = ''
        if billion:        
            result = threeHelper(billion) + ' Billion'
        if million:
            result += ' ' if result else ''    
            result += threeHelper(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += threeHelper(thousand) + ' Thousand'
        if hundred:
            result += ' ' if result else ''
            result += threeHelper(hundred)
        return result
        