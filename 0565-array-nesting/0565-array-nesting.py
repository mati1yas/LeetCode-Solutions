class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        self.memo={}
        self.long=0
        def dfs(index,nest):
            
            if nums[index] not in nest and nums[index] not in self.memo:
                nest.add(nums[index])
                m=dfs(nums[index],nest)
                self.memo[nums[index]]=m
            elif nums[index] in self.memo:  
                return self.memo[nums[index]]
            else:
                self.long=max(self.long,len(nest))
                return 
                
            
            
            
            
        
        for i in range(len(nums)):
            s=set()
            s.add(nums[i])
            dfs(nums[i],s)
        return self.long