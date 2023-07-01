class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        
        self.ans=float('inf')
        def backtrack(index,arr ,ungiven):
            if len(cookies) - index < ungiven:
                return 
            if index >= len(cookies):
                self.ans=min(self.ans,max(arr))
                return 
            
            for i in range(len(arr)):
                ungiven -= int(arr[i] == 0)
                arr[i]+=cookies[index]
                backtrack(index+1,arr,ungiven)
                arr[i]-=cookies[index]
                ungiven += int(arr[i] == 0)
                
        
        arr=[0 for i in range(k)]
                
        backtrack(0,arr,k)
        return self.ans