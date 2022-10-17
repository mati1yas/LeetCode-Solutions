class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        self.steps={}
        self.memo={}
        def dfs(num,op,x):
            if num==1:
                return 0
            if num<1:
                return 
            if num not in self.memo:
                if num%2==0:
                    x=dfs(num//2,op+1,x)

                else:
                    x=dfs(num*3+1,op+1,x)
            
                self.memo[num]=x+1
            else:
                self.steps[x]=self.memo[num]+op
                
            return self.memo[num]
        
        arr=[]
        for i in range(lo,hi+1):
            arr.append(i)
            dfs(i,0,i)
            self.steps[i]=dfs(i,0,i)
        
        arr.sort(key=lambda x:self.steps[x])
        
        return arr[k-1]