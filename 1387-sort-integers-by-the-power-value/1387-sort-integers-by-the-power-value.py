class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        self.steps={}
        def dfs(num,op,x):
            if num==1:
                self.steps[x]=op
                return
            if num<1:
                return 
            
            if num%2==0:
                dfs(num//2,op+1,x)
            
            else:
                dfs(num*3+1,op+1,x)
            
            
        
        arr=[]
        for i in range(lo,hi+1):
            arr.append(i)
            dfs(i,0,i)
        
        arr.sort(key=lambda x:self.steps[x])
        
        return arr[k-1]