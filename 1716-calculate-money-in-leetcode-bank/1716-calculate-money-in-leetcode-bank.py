class Solution:
    def totalMoney(self, n: int) -> int:
        
        
        def calculateWeeklyTotal(start,end,n):
                       
            return (n*(start+end))//2
        
        
        
        total=0
        lastStart=1 
        while n :
            
            if n-7>=0:
                
                total+=calculateWeeklyTotal(lastStart,lastStart+6,7)
                n-=7
            else:
                total+=calculateWeeklyTotal(lastStart,lastStart+n-1,n)
                n=0
            lastStart+=1
            
        return total 
                