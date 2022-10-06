class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        
        self.r=0
        def triangle(arr):
            
            
            
            if len(arr)==1:
                self.r=arr[0]
                return 
            
            newarr=[]
            
            if len(arr)==2:
                newarr=[sum(arr)%10]
                triangle(newarr)
            else:
                p1=0
                p2=1

                while p2<len(arr):
                    newarr.append((arr[p1]+arr[p2])%10)
                    p1+=1
                    p2+=1
                
                triangle(newarr)
        triangle(nums)
        return self.r