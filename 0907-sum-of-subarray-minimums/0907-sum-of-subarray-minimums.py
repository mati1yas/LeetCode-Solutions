class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        
        stack=[]
        
        total = 0
        for i in range(len(arr)+1):
            
            while stack and (i==len(arr) or arr[stack[-1]]>=arr[i]):
                
                cur=stack.pop()
                
                leftBound=-1 if not stack else stack[-1]
                rightBound=i
                
                arrRange=(cur-leftBound)*(rightBound-cur)
                
                total+=(arrRange*arr[cur])
            stack.append(i)
        
        return total%(10**9+7)