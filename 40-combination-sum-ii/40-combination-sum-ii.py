class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        
        
        self.combs=[]
        
        def comb (index,arr,tot):
            if tot>target:
                return
            if tot==target:
                self.combs.append(arr)
                return 
            
            for i in range(index,len(candidates)):
#                 this is to make sure that at this level considering duplicate is just a waaste of time and it is to avoid the duplication
# at the other level tho duplicates can exist in the combo
                if i>index and candidates[i]==candidates[i-1]:
                    continue
                comb(i+1,arr+[candidates[i]],tot+candidates[i])
            
            
            
            
            
        
        candidates.sort()
        
        comb(0,[],0)
        return self.combs