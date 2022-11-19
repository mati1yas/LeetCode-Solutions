class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        
        res=[]
        for i in range(len(r)):
            start=l[i]
            end=r[i]
            arr=nums[start:end+1]
            arr.sort()
            
            diff=None
            failed=None
            for j in range(1,len(arr)):
                
                if diff==None:
                    diff=arr[j]-arr[j-1]
                    
                elif diff!=arr[j]-arr[j-1] :
                    failed=True
                    res.append(False)
                    break
                
            if not failed:
                res.append(True)
        return res
                
                    
            
            