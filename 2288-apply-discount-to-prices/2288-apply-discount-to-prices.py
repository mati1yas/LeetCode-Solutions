class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        arr=sentence.split(' ')
        ret=[]
        
        for word in arr:
            if word[0]=="$" and word[1:].isdigit():
                price=int(word[1:])
               
                ret.append("$"+"{:.2f}".format(price- (discount/100)*price))
                
            else:
                ret.append(word)
        
        return " ".join(ret)