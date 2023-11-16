class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        
        
        def helper(nums1,nums2,swapped):
            
            if swapped:
                swap=1
            else:
                swap=0
            
            for i in range(len(nums1)-1):
                
                if nums1[n-1] >= nums1[i] and  nums2[n-1]>= nums2[i]:
                    continue

                elif nums1[n-1] >= nums2[i] and  nums2[n-1] >= nums1[i]:

                    swap+=1

                else:
                    return -1
                
            return swap

            
                
            
            
            
        n=len(nums1)   
        
        result1 = helper(nums1,nums2,False)
        
        print(nums1,nums2)
        nums1[n-1], nums2[n-1]= nums2[n-1],nums1[n-1]
        print(nums1,nums2)
        result2 = helper(nums1,nums2,True)
        
        
        if result1==-1 and result2==-1:
            return -1
        
        elif result1==-1:

            return result2
            
        elif result2 == -1:

            return result1
        
        
        return min(result1,result2)
            
        
            
            
            
            
            
            
            