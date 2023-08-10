class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        
        """
         |
        [1,0,1,1,1]
           |     
             |

        """
        
        
        left=0
        right=len(nums)-1
        
        
        while left<=right:
            
            while left<=right and nums[left]==nums[right]:
                
                left+=1
                
                
            
            mid=(left+right)//2
            
            if left>right and nums[mid]!=target :
                
                return False
            if nums[mid]==target:
                return True
            
            
            
            if nums[left]<=nums[mid]:
                
                if nums[left]<=target<=nums[mid]:
                    
                    right=mid-1
                    
                else:
                    left=mid+1
            else:
                
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
                    
            
                    
                
                
        return False