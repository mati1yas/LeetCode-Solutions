class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0:
            return 0
        
        isPrime=[True]*(n+1)
        
        isPrime[0]=False
        isPrime[1]=False
        primesCount=0
        for i in range(2,n):
            
            if isPrime[i]:
                primesCount+=1
                for j in range(i+i,n,i):
                    isPrime[j]=False
        
        return primesCount