class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        numbers=set(arr)
        for num  in range(1,2**31-1):
            
            if num not in numbers:
                k-=1
            
            if k==0:
                return num
            