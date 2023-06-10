class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        left=1
        right=maxSum
        
        
        def calcSum(start,n):
            
            total=(n/2)*((start*2)+(n-1))
            
            
            
            
            return total
        ans=0
        while left <= right:
            
            
            target = (left+right) // 2
            
            
            left_val=target-index
        
            right_val=target-(n-index-1)
            leftTotal=0
            rightTotal=0
            
            
            if left_val<=0:
                ones=abs(left_val)+1                
                leftTotal=calcSum(1,target)+ones                
            else:
                
                leftTotal=calcSum(left_val,index+1)
                
             
            
            
            
            if right_val<=0:
                ones=abs(right_val)+1
                
                rightTotal=calcSum(1,target)+ones
                  
            else:
                 
                rightTotal=calcSum(right_val,target-right_val+1)
                
                
                
                
                
                
            
            if leftTotal+rightTotal-target <= maxSum:
                
                ans=max(ans,target)
                left=target+1
                
            else:
                right=target-1
                
        return ans
                
                
            
            
        