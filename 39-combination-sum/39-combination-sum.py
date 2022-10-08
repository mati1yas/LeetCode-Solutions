class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        self.combs=[]
        def comb(arr,tot):
            
            if tot>target:
                return 
            if tot==target:
                if sorted(arr) not in self.combs:
                    self.combs.append(sorted(arr))
                
            for node in candidates:
                comb(arr+[node],tot+node)
            
            
            
            
            
            
            
            
        
        for node in candidates:
            comb([node],node)
        return self.combs