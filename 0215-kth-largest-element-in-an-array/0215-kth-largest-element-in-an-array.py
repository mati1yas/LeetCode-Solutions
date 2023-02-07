class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        
        arr=[0 for _ in range(20000+1)]
        
        for num in nums:
            arr[num+10000]+=1
            
        
        count=0
        for i in range(len(arr)-1,-1,-1):
            count+=arr[i]
            if count>=k:
                return i-10000
                break
                
        return 0