class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        

        invalidSet=set()

        personTransaction=defaultdict(list)

        
        for i,valid in enumerate(transactions):
            name,time,amount,city=valid.split(',')
            if int(amount)>1000:
                    invalidSet.add(i)


            for j in personTransaction[name]:

                

                name2,time2,amount2,city2=transactions[j].split(',')

                if int(amount)>1000:
                    invalidSet.add(i)

                
                if city2!=city and abs(int(time2)-int(time))<=60:
                    invalidSet.add(i)
                    invalidSet.add(j)
            personTransaction[name].append(i)
            
        

        return [transactions[j] for j in list(invalidSet)]
