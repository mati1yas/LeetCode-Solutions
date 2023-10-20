class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        
        
        new_arr= set(arr)
        
        
        new_arr=list(new_arr)
        new_arr.sort()
        rankMap={}
        for i,val in enumerate(new_arr):
            rankMap[val]=i+1
        
        
        for i in range(len(arr)):
            
            arr[i]=rankMap[arr[i]]
            
        return arr
            
        
        
